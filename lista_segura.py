"""Lista Segura: adiciona itens sem alterar a lista original (cópia defensiva)."""


def adicionar_item_seguro(lista_original, item):
    """Retorna uma NOVA lista com o item adicionado, sem modificar a original."""
    nova_lista = lista_original.copy()
    nova_lista.append(item)
    return nova_lista


def adicionar_item(item, lista=None):
    """Adiciona item a uma lista, evitando lista mutável como valor padrão."""
    if lista is None:
        lista = []
    lista.append(item)
    return lista


if __name__ == "__main__":
    frutas = ["maçã", "banana"]
    novas_frutas = adicionar_item_seguro(frutas, "uva")
    print(f"Original: {frutas}")
    print(f"Nova:     {novas_frutas}")
