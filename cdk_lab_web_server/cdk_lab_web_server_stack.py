from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_ec2 as ec2,
)
from constructs import Construct

class CdkLabWebServerStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create VPC with public subnet
        vpc = ec2.Vpc(
            self, "cdk_lab_vpc",
            cidr="10.0.0.0/16",
            max_azs=1,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PUBLIC,
                    name="PublicSubnet01",
                    cidr_mask=24,
                )
            ],
        )

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "CdkLabWebServerQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
