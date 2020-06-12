import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

def collate_fn(batch):
    return tuple(zip(*batch))

def plot_boxes(image, boxes, color):
    plt.imshow(image)
    for box in boxes:
        rect = Rectangle((box[0],box[1]),box[2]-box[0],box[3]-box[1],linewidth=1,edgecolor=color,facecolor='none')
        plt.axes().add_patch(rect)
    plt.show()
    
def get_model_name(epoch, score, loss):
    return "GWD_EPOCH_{0}_SCORE_{1:.4f}_LOSS_{2:.4f}.pt".format(epoch, score, loss)
    
def format_prediction_string(boxes, scores):
    pred_strings = []
    for j in zip(scores, boxes):
        #pred_strings.append("{0:.4f} {1:.0f} {2:.0f} {3:.0f} {4:.0f}".format(j[0], j[1][0], j[1][1], j[1][2]-j[1][0], j[1][3]-j[1][1]))
        pred_strings.append("{0} {1} {2} {3} {4}".format(j[0], j[1][0], j[1][1], j[1][2]-j[1][0], j[1][3]-j[1][1]))
    return " ".join(pred_strings)


def remove_blanks(images, targets):
    indices = []
    for i in range(len(targets)):
        if targets[i]['labels']==np.array([], dtype=np.int64):
            print('Blank Pointed')
            indices.append(i)
    indices = indices[::-1]
    for indice in indices:
        print(indice)
        images.pop(indice)
        targets.pop(indice)
    print(len(targets))
    return images, targets

def is_contain_blanks(targets):
    for i in range(len(targets)):
        if targets[i]['labels']==np.array([], dtype=np.int64):
            print('Found a blank image')
            return True
    return False
    
    