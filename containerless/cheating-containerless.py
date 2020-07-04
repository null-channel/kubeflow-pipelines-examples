import kfp
from kfp import dsl


@dsl.pipeline(name='my-pipeline')
def pipeline():
    op0 = dsl.ContainerOp(
        name="gen-numbers",
        image='python:alpine3.6',
        command=["sh", "-c"],
        arguments=[
            'python -c "import random; import json; import sys; json.dump([i for i in range(20, 26)], open(\'/tmp/out.json\', \'w\'))"'],
        file_outputs={'out': '/tmp/out.json'},
    )

    with dsl.ParallelFor(op0.output) as item:
        op1 = dsl.ContainerOp(
            name="my-item-print",
            image="library/bash:4.4.23",
            command=["sh", "-c"],
            arguments=["echo do output op1 item: %s" % item],
        )

    op_out = dsl.ContainerOp(
        name="total",
        image="python:alpine3.6",
        command=["sh", "-c"],
        arguments=['echo output gen-numbers: %s && python -c "print(sum(%s))"' % (op0.output, op0.output)],
    )


if __name__ == '__main__':
    kfp.compiler.Compiler().compile(pipeline, __file__ + '.yaml')
