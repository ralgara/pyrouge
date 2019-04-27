#!/usr/bin/env python3

from pprint import pprint
from os import path
import sys
sys.path.append(path.abspath(__file__))
from pyrouge import Rouge155

ref_texts = {'A': "Poor nations pressurise developed countries into granting trade subsidies.",
             'B': "Developed countries should be pressurized. Business exemptions to poor nations.",
             'C': "World's poor decide to urge developed nations for business concessions."}
summary_text = "Poor nations demand trade subsidies from developed nations."

if __name__ == '__main__':
    rouge = Rouge155(n_words=100)
    score = rouge.score_summary(summary_text, ref_texts)
    pprint(score)
