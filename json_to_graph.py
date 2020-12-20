# 複数のjsonファイルからグラフを出力する。引数は入力数、入力ファイル名、カラー、xyのラベル名と出力ファイル名
import argparse
import json
import numpy as np
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description='Output some graphs.')

parser.add_argument('-i','--input', action='store', type=str, nargs='*')
parser.add_argument('-n','--name', action='store', type=str, nargs='*')
parser.add_argument('-y','--extname', action='store', default=None, type=str, nargs='*')
parser.add_argument('-c','--color', action='store', default=None, type=str, nargs='*')
parser.add_argument('-o','--output', default='graph.png')
parser.add_argument('-s','--smoothed', type=bool, default=True)
parser.add_argument('-f', '--factor', type=float, default=0.999)
parser.add_argument('-xl', '--xlabel', type=str)
parser.add_argument('-yl', '--ylabel', type=str)


args = parser.parse_args()
#args = parser.parse_args("-i openaigym.episode_batch.0.582126.stats.json openaigym.episode_batch.0.601630.stats.json -n RND PADDPG -y episode_rewards episode_rewards -c red blue".split())
#args = parser.parse_args("-i aa bb -n cc dd -c a b".split())
def smoothed(points, factor=args.factor):
    smoothed_points = []
    for point in points:
        if smoothed_points:
            previous = smoothed_points[-1]
            smoothed_points.append(previous * factor + point * (1 - factor))
        else:
            smoothed_points.append(point)
    return smoothed_points


# TODO: 色の自動振り分けほしい
def main():
    fig = plt.figure(figsize=(12.8, 7.2))
    # input の数だけgraph作成
    for index,i in enumerate(args.input):
        f = open(i, 'r')
        json_data = json.load(f)
        y = json_data[args.extname[index]]
        if args.smoothed:
            y = smoothed(y)
        x = range(0, len(y))
        plt.plot(x, y, label=args.name[index], color=args.color[index])
    plt.xlabel(args.xlabel, fontsize=18)
    plt.ylabel(args.ylabel, fontsize=18)
    plt.legend(fontsize=18)
    plt.tick_params(labelsize=18)
    plt.tight_layout()
    plt.grid(which='major', color='gray', linestyle='-')
    plt.savefig(args.output, dpi=300)
    plt.show()

if __name__=="__main__":
    main()
