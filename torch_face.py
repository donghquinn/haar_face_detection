import torch.nn as nn
from torch.nn import functional as F
from utils_resnet import resnet18

class FaceNet_ResNet18(nn.Module):
    def __init__(self, embedding_dimension=128, pretrained=False):
        super().__init__()
        self.model = resnet18(pretrained=pretrained)
        
        # embedding
        input_features_fc_layer = self.model.fc.in_features # fc layer 채널 수 얻기
        self.model.fc = nn.Linear(input_features_fc_layer, embedding_dimension, bias=False) # fc layer 수정
        
    def forward(self, images):
        embedding = self.model(images) # embedding 생성
        embedding = F.normalize(embedding, p=2, dim=1) # normalize
        return embedding