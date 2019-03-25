esta_chovendo = False

#True é o mais próximo
print("Hoje estou com as roupas " +
      ("secas.", "molhadas.")[esta_chovendo])


print("Hoje estou com as roupas " +
      ("molhadas." if esta_chovendo else "secas."))