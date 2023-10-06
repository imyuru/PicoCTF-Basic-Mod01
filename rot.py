def rot13_decodificador(text):
    texto = ''
    for char in text:
        if 'a' <= char <= 'z':
            decodificada = chr(((ord(char) - ord('a') - 13) % 26) + ord('a'))
        elif 'A' <= char <= 'Z':
             decodificada = chr(((ord(char) - ord('A') - 13) % 26) + ord('A'))
        else:
             decodificada = char
        texto +=  decodificada
    return texto

textoDecodificado = rot13_decodificador("cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_nSkgmDJE}")
print(textoDecodificado)
