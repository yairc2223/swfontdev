from fontTools.voltLib.parser import Parser
from fontTools.feaLib.builder import addOpenTypeFeatures
from fontTools.ttLib import TTFont


font = TTFont("SuttonSignWritingOneD.ttf")

addOpenTypeFeatures(font, "project.fea")

font.save("font.ttf")