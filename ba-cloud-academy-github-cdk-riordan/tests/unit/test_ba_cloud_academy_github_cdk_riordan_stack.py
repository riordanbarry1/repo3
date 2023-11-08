import aws_cdk as core
import aws_cdk.assertions as assertions

from ba_cloud_academy_github_cdk_riordan.ba_cloud_academy_github_cdk_riordan_stack import BaCloudAcademyGithubCdkRiordanStack

# example tests. To run these tests, uncomment this file along with the example
# resource in ba_cloud_academy_github_cdk_riordan/ba_cloud_academy_github_cdk_riordan_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = BaCloudAcademyGithubCdkRiordanStack(app, "ba-cloud-academy-github-cdk-riordan")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
