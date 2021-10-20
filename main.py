import matplotlib.pyplot as plt

def pokolenia(x):
    return x * 0.01 * 40

def average_function(data):

    sum = 0
    for i in data:
        sum += float(i)
    return sum / len(data) * 100

def loading_file(path):

    try:
        file = open(path)
    except IOError:
        print("File not found or path is incorrect")
    finally:
        x = []
        y = []
        box = []
        file.readline()
        for line in file:
            line = line.replace("\n", "").split(",")
            x.append(int(line[1]) * 0.001)
            y.append(average_function(line[2:]))
            box.append([float(x) * 100 for x in line[2:]])

        file.close()
        return x, y, box

def main():

    cel2_x, cel2_y, cel2_box = loading_file("2cel.csv")
    celRS2_x, celRS2_y, celRS2_box = loading_file("2cel-rs.csv")
    cel_x, cel_y, cel_box = loading_file("cel.csv")
    celRS_x, celRS_y, celRS_box = loading_file("cel-rs.csv")
    rsel_x, rsel_y, rsel_box = loading_file("rsel.csv")
    fig, (plt1, plt2) = plt.subplots(1, 2, figsize = (6.7, 6.7))
    plt.rcParams.update({'font.family': 'Times New Roman'})
    n = 25

    plt1.plot(rsel_x, rsel_y, c="blue", label='1-Evol-RS', marker = "o",
              markevery = n, markeredgecolor = 'black', markersize = 5, alpha = 0.8, linewidth = 0.8, markeredgewidth = 0.5)
    plt1.plot(celRS_x, celRS_y, c="green", label='1-Coev-RS', marker = "v",
              markevery = n, markeredgecolor = 'black', markersize = 5, alpha = 0.8, linewidth = 0.8, markeredgewidth = 0.5)
    plt1.plot(celRS2_x, celRS2_y, c="red", label='2-Coev-RS', marker = "D",
              markevery = n, markeredgecolor = 'black', markersize = 5, alpha = 0.8, linewidth = 0.8, markeredgewidth = 0.5)
    plt1.plot(cel_x, cel_y, c = "black", label='1-Coev', marker = "s",
              markevery = n, markeredgecolor = 'black', markersize = 5, alpha = 0.8, linewidth = 0.8, markeredgewidth = 0.5)
    plt1.plot(cel2_x, cel2_y, c="fuchsia", label='2-Coev', marker = "d",
              markevery = n, markeredgecolor = 'black', markersize = 5, alpha = 0.8, linewidth = 0.8, markeredgewidth = 0.5)
    plt1.grid(linestyle = "dashed", linewidth = 0.3)
    plt1.set_xlim(0, 500)
    plt1.set_ylim(60, 100)
    plt1.legend(loc = 'lower right', numpoints = 2, edgecolor = 'grey')
    plt1.set_xticks([0, 100, 200, 300, 400, 500])
    plt1.set_xlabel("Rozegranych gier (x1000)")
    plt1.set_ylabel("Odsetek wygranych gier [%]")
    plt1.tick_params(direction="in", top = True, right = True)
    secax = plt1.secondary_xaxis('top', functions=(pokolenia, pokolenia))
    secax.set_xlabel("Pokolenia")
    secax.set_xticks([0, 40, 80, 120, 160, 200])
    secax.tick_params(direction="in")

    date = [rsel_box[199], celRS_box[199], celRS2_box[199], cel_box[199], cel2_box[199]]
    whiskerprops = dict(linestyle=(0, (5, 6)), color='b', linewidth=0.8)
    flierprops = dict(marker='+', markerfacecolor='b', linestyle='none', markeredgecolor='b')
    medianprops = dict(color='firebrick', linewidth=1.5)
    meanprops = dict(marker='o', markeredgecolor='black', markerfacecolor='b')
    boxprops = dict(color='b')
    plt2.boxplot(date, boxprops=boxprops, whiskerprops=whiskerprops, notch=True, medianprops=medianprops,
                    flierprops=flierprops, meanprops=meanprops, showmeans=True)
    name = plt.setp(plt2, xticklabels=['1-Evol-RS', '1-Coev-RS', '2-Coev-RS', '1-Coev', '2-Coev'])
    plt.setp(name, rotation=30, fontsize=8)
    plt2.get_yaxis().tick_right()
    plt2.grid(linestyle='dashed', linewidth = 0.3)
    plt2.set_ylim(60, 100)

    plt.savefig('myplot.pdf')
    plt.close()


if __name__ == '__main__':
    main()
