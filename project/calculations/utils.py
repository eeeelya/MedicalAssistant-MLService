import datetime
import io
import json

import boto3
import numpy as np

from project.models import LaunchModel
from project.extensions import db
from project.config import AWS_KEY, AWS_SECRET_KEY, AWS_REGION, RESULTS_BUCKET


def create_launch(model: str, image_name: str, image_height: int, image_width: int, success: bool):
    record = LaunchModel(
        model=model,
        date=datetime.datetime.now(),
        image_name=image_name,
        image_height=image_height,
        image_width=image_width,
        success=success,
    )

    db.session.add(record)
    db.session.commit()


def upload_result_to_s3(file, filename):
    s3 = boto3.client("s3", aws_access_key_id=AWS_KEY, aws_secret_access_key=AWS_SECRET_KEY, region_name=AWS_REGION)

    s3.put_object(
        Body=file,
        Bucket=RESULTS_BUCKET,
        Key=filename,
        ContentType="image/png",
        ACL="public-read",
    )

    return f"https://{RESULTS_BUCKET}.s3.{AWS_REGION}.amazonaws.com/{filename}"


def save_results(mask, filename: str):
    with io.BytesIO() as temp:
        mask.save(temp, format="png")
        temp.seek(0)
        s3_url = upload_result_to_s3(temp, f"{filename}_result_mask.png")
    return s3_url


def start_segmentation(model_name: str, image: np.ndarray):
    aws_lambda = boto3.client(
        "lambda", aws_access_key_id=AWS_KEY, aws_secret_access_key=AWS_SECRET_KEY, region_name=AWS_REGION
    )
    parameters = {
        "model_name": model_name,
        "image": image.tolist(),
    }

    result = aws_lambda.invoke(
        FunctionName="model-predictions-new",
        InvocationType="RequestResponse",
        Payload=json.dumps(parameters),
    )
    response = json.loads(result["Payload"].read())

    return response
