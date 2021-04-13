import matplotlib.pyplot as plt 
from matplotlib import style


def fibbonacci_loop(number):
    start =1
    new, old = start,start
    for itr in range(number - 1):
        temp = new
        new = old 
        old = old + temp 
    return new 

def rabbits_and_recursion(months, offspring):
    parent, child = 1,1
    for itr in range(months - 1):
        child,parent = parent, parent + child*offspring
    return child 

def rabbit_data_pop(offspring,end_month):
    f = open(f'k{offspring}.txt','w+')
    #f.write('k={}\n'.format(offspring))
    for month in range(end_month):
        pop = rabbits_and_recursion(month, offspring)
        f.write(f'{month},{pop}\n')
    f.close()

def rabbit_graph(num_files):
    style.use('fivethirtyeight')
    fig=plt.figure(figsize =(6,2))
    fig.set_size_inches(18.5,10.5,forward=True)
    ax1 = fig.add_subplot(111)
    for i in range(1,num_files+1):
        graph_data = open(f'k{i}.txt','r').read()
        lines = graph_data.split('\n')
        xs1=[]
        ys1=[]
        for line in lines:
            if len(line)>1:
                x,y =line.split(',')
                xs1.append(float(x))
                ys1.append(float(y))
        ax1.plot(xs1,ys1)
    ax1.set(xlabel = 'time step (n)', ylabel = 'population',
            title = 'Rabbit Population Growth' )
    fig.set_figheight(96)
    fig.set_figwidth(24)
    fig.subplots_adjust(left=.15,right =.8,bottom=.2,top=.85)
    plt.show()

def main():
    time_steps =15
    num_of_offspring = range(1,5)
    for i in num_of_offspring:
        rabbit_data_pop(i,time_steps)
        print('k={}'.format(i))
    rabbit_graph(len(num_of_offspring))
    

if __name__ == '__main__':
    main()





