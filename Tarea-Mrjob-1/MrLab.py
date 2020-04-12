from mrjob.job import MRJob

class Mrlab(MRJob):

    def mapper(self, _, line):
        if(line.split(",")[2].isdigit()):
            yield("empleado: "+line.split(",")[0], int(line.split(",")[2]))
            yield("SE: "+line.split(",")[1], int(line.split(",")[2]))
            yield("Emp/SE: "+line.split(",")[0], int(1))

    def combiner(self, key, values):
        yield (key, sum(values))

    def reducer(self, key, values):
        if(str(key).split(":")[0]=="Emp/SE"):
            yield key, sum(values)
        else:
            avg=0
            con=0
            for x in values:
                avg+=x
                con+=1
            avg/=con
            yield key, avg

if __name__ == '__main__':
    Mrlab.run()