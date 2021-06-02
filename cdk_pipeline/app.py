#!/usr/bin/env python3

from aws_cdk import core as cdk
from my_pipeline.my_pipeline_stack import MyPipelineStack

app = core.App()
MyPipelineStack(
    app,
    'cdk_pipeline',
)
app.synth()
