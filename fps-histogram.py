__author__ = 'Sam'

import glob
import os
import re
from ascii_graph import Pyasciigraph


def draw_graph(fps):
    histo_graph = []
    pre = 0
    for f in fps:
        count = 0
        if f == pre:
            count += 1
            print("incremented")
        else:
            count = 1
        pre = f
        print(count)



def read_log(name):
    file = open(name, 'r')
    fps = []
    mean = 0.0
    for line in file:
        match = re.search(r'(?P<value>\d{1,2}\.\d{1,2})\sFPS@640x480', line)
        # match = re.search(r'.*FPS@640x480', line)
        if match:
            fps.append(float(match.group('value')))
            mean = float(sum(fps))/len(fps) if len(fps) > 0 else float('nan')
            # print("Name: " + name + " | FPS: " + match.group('value') + " | %.2f" % mean)
    print("Name: " + name + " | Mean: %.2f" % mean)
    # draw_graph(fps)


def main():
    os.chdir(r'C:\Users\Sam\Desktop\comsys')
    # List of ".txt" files
    names = glob.glob('*.txt')
    for name in names:
        read_log(name)
    draw_graph([6, 6, 7])
    # test = [('long_label', 2.49), ('sl', 2.407), ('line3', 2.88), ('line4', 1.053), ('line5', 1.22)]
    # graph = Pyasciigraph()
    # for line in graph.graph('Fps', test):
    #     print(line)

if __name__ == '__main__':
    main()




