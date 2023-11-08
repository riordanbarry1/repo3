from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_s3 as s3,
    RemovalPolicy,
)
from constructs import Construct


class BaCloudAcademyGithubCdkRiordanStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        bucket = s3.Bucket(
            self,
            'bucket-object',
            bucket_name='riordanbucketagainagainagainagainagain',
            removal_policy=RemovalPolicy.DESTROY,
        )
