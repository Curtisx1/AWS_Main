import aws_cdk as cdk
import aws_cdk.aws_s3 as s3

from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
)
from constructs import Construct

class WebAppStack(cdk.Stack):

    def __init__(self, scope: cdk.App, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "WebAppQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
        bucket = s3.Bucket(self, "MyFirstBucket", versioned=True)