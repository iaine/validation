class SonicDF():

    def checkType(self, data, checktype):
        '''
           Simple check to see if a type is expected
        '''
        if isinstance(checktype, list):
            return self.check_array(data, checktype)
        else:
            return self.check_single(data, checktype)

    def check_single(self, data, checktype):
        return isinstance(data, checktype)

    def check_array(self, data, checktype):
        
        if len(checktype) == 1:
            for i in xrange(len(data)-1):
                if self.check_single(data[i], checktype[0]) == False:
                    return False
        else:
            if len(data) != len(checktype):
                raise Exception("Lengths must be the same")
            for i in xrange(len(data)):
                print(checktype[i])
                print(self.check_single(data[i], checktype[i]))
                if self.check_single(data[i], checktype[i]) == False:
                    return False

        return True
