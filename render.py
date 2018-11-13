#!/usr/bin/env python3

import graphviz
from sklearn import tree
import model


TARGET_NAMES = [ "o",
            "w",
            "n",
            "e",
            "s" ]

FEATURE_NAMES = ['PERCENTAGE_DONE', 'LOCAL', 'LOCAL',
            'LOCAL', 'LOCAL', 'LOCAL', 'LOCAL',
            'LOCAL', 'LOCAL', 'LOCAL', 'LOCAL',
            'LOCAL', 'LOCAL', 'LOCAL', 'LOCAL',
            'LOCAL', 'LOCAL', 'HIGHEST_HALITE', 'HIGHEST_HALITE',
            'HIGHEST_HALITE', 'HIGHEST_HALITE',
            'HIGHEST_HALITE', 'HIGHEST_HALITE',
            'HIGHEST_HALITE', 'HIGHEST_HALITE',
            'HIGHEST_HALITE', 'HIGHEST_HALITE',
            'HIGHEST_HALITE', 'HIGHEST_HALITE',
            'HIGHEST_HALITE', 'HIGHEST_HALITE',
            'HIGHEST_HALITE', 'HIGHEST_HALITE',
            'HIGHEST_HALITE', 'HIGHEST_HALITE',
            'HIGHEST_HALITE', 'HIGHEST_HALITE',
            'HIGHEST_HALITE', 'HIGHEST_HALITE',
            'HIGHEST_HALITE', 'HIGHEST_HALITE',
            'HIGHEST_HALITE', 'HIGHEST_HALITE',
            'HIGHEST_HALITE', 'HIGHEST_HALITE',
            'HIGHEST_HALITE', 'HIGHEST_HALITE',
            'HIGHEST_HALITE', 'HIGHEST_HALITE',
            'HIGHEST_HALITE', 'HIGHEST_HALITE',
            'HIGHEST_HALITE', 'HIGHEST_HALITE',
            'HIGHEST_HALITE', 'HIGHEST_HALITE',
            'HIGHEST_HALITE', 'HIGHEST_HALITE',
            'HIGHEST_HALITE', 'HIGHEST_HALITE',
            'HIGHEST_HALITE', 'HIGHEST_HALITE',
            'HIGHEST_HALITE', 'HIGHEST_HALITE',
            'HIGHEST_HALITE', 'HIGHEST_HALITE',
            'CLOSEST_DROP_OFF', 'CLOSEST_DROP_OFF',
            'CLOSEST_DROP_OFF', 'CLOSEST_DROP_OFF',
            'LOCAL_AREA', 'LOCAL_AREA', 'LOCAL_AREA', 'LOCAL_AREA',
            'CURRENT_CELL', 'CURRENT_CELL',
            'CURRENT_CELL', 'CURRENT_CELL', 'CURRENT_CELL']

def main():

    bot = model.HaliteModel(weights="out/dt.svc")

    dot_data = tree.export_graphviz(bot.model,
                out_file="out/dt.dot", feature_names=FEATURE_NAMES,
                class_names=TARGET_NAMES,
                filled=True, rounded=True, special_characters=True)
    print("Dot file generated at out/dt.dot. Please run util/render.sh to generate a png file.")

if __name__ == "__main__":
    main()

