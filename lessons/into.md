#Intro to pipelines

Kubeflow pipelines are one of the largest parts of kubeflow. There are really two sides too the pipeline, The actual pipelines that get run and viewed, and the tools used to create them. A kubeflow pipeline is just like any other pipeline like jenkins, a description of a set of tasks to be accomplished to produce the final desired state.

Pipelines are made up of the pipeline and it's components. 

The pipeline describes each components inputs and outputs and how they relate
The components are indevidual tasks that need to be accomplished on the defined inputs, each component is itself a container.
