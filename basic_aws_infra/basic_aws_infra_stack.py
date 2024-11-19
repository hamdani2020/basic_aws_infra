from aws_cdk import (
    RemovalPolicy,
    # aws_sqs as sqs,
    # Duration,
    Stack,
)
from aws_cdk import (
    aws_ec2 as ec2,
)
from aws_cdk import (
    aws_s3 as s3,
)
from constructs import Construct


class BasicAwsInfraStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "BasicAwsInfraQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
        vpc = ec2.Vpc(
            self,
            "FirstVpc",
            max_azs=2,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="PublicSubnet", subnet_type=ec2.SubnetType.PUBLIC, cidr_mask=24
                )
            ],
        )

        instance = ec2.Instance(
            self,
            "MyInstance",
            instance_type=ec2.InstanceType("t2.micro"),
            machine_image=ec2.MachineImage.latest_amazon_linux(),
            vpc=vpc,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),
        )

        bucket = s3.Bucket(
            self, "DataBucket", versioned=True, removal_policy=RemovalPolicy.DESTROY
        )
