#necessario instalar as blibliotecas 'qrcode' e 'image'
import qrcode
##import image

imagem = qrcode.make('https://www.youtube.com/watch?v=6R3ouGNcACQ')
imagem.save('imagemqr.png')
imagem.show()