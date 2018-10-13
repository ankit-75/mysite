def print_everything(**args):
        print(args)
        # for count, thing in enumerate(args):
        #    print( '{0}. {1}'.format(count, thing))
        for name, value in args.items():
           print( '{0} = {1}'.format(name, value))

print_everything(apple='apple',banana='banana')
#print_everything('apple','banana')