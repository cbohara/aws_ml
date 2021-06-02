import aws_cdk.core as cdk
from aws_cdk.core import Stack, StackProps, Construct, SecretValue
from aws_cdk.pipelines import CdkPipeline, SimpleSynthAction

import aws_cdk.aws_codepipeline as codepipeline
import aws_cdk.aws_codepipeline_actions as codepipeline_actions


class CdkPipelineStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        source_artifact = codepipeline.Artifact()
        cloud_assembly_artifact = codepipeline.Artifact()

        pipeline = CdkPipeline.CdkPipeline(
	        self,
	        'Pipeline',
	        pipeline_name='MyAppPipeline',
	        cloud_assembly_artifact=cloud_assembly_artifact,
	        source_action=cpa.GitHubSourceAction(
		        action_name='Github',
		        output=source_artifact,
		        oauth_token=cdk.SecretValue.secrets_manager('GITHUB_TOKEN_NAME'),
		        trigger=cpa.GitHubTrigger.POLL,
		        owner='cbohara',
		        repo='aws_projects'
	        ),
			synth_action=SimpleSynthAction.standard_npm_synth(
				source_artifact=source_artifact,
				cloud_assembly_artifact=cloud_assembly_artifact
			)
		)
