import torch
import numpy as np

a = torch.tensor([0,1,2,3,4]) # criar tensor

print(a.dtype) # ver tipo do conteudo do tensor
print(a.type()) # ver tipo do tensor

b = torch.tensor([0.0,1.0,2.0,3.0,4.0], dtype= torch.int32) # definir o tipo do tensor
# ou
c = torch.FloatTensor([0,1,2,3,4]) # para obter o mesmo resultado
# definindo esse tipo ao rodar o tensor ajusta ao seu tipo

print(b.type())
print(c.type())

# Se quiser muda o tipo do tensor so rodar

d = torch.tensor([0,1,2,3,4])
d = d.type(torch.FloatTensorS)

# ver quantos itens tem em um tensor

print(d.size()) # output 5

# ver quantos dimensoes o tensor possui

print(d.ndimension()) # output 1

# converter tensores 1d para 2d

e = torch.Tensor([0,1,2,3,4,5])

e_col = e.view(6,1) #tamnanho x e y
# ou
e_col = e.view(-1,1)

# convertendo np array para tensores

numpy_array = np.array([0.0,1.0,2.0,3.0,4.0])
torch_tensor = torch.from_numpy(numpy_array)
# converter de novo para numpy
back_numpy=torch_tensor.numpy()