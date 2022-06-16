import kfp
from kfp import dsl

def NestApp_op():

    return dsl.ContainerOp(
        name='NextAppJS',
        image='gcr.io/original-guru-350415/pelvic_test_2:NestApp',
        command=["sh", "-c"],
        arguments=["echo First Operation Successful"],
        file_outputs={}
    )

def PyApp_op():

    return dsl.ContainerOp(
        name='PyApp',
        image='gcr.io/original-guru-350415/pelvic_test_1:latest',
        command=["sh", "-c"],
        arguments=["echo Second operation Succesful"],
        file_outputs={}
    )


@dsl.pipeline(
   name='Testing Pipeline',
   description='An example pipeline that combines NestApp and PyApp'
)
def pipeline():
    NestApp_op()
    PyApp_op()


if __name__ == '__main__':
    kfp.compiler.Compiler().compile(pipeline, __file__ + '.yaml')