# Teoria de `CSS` - **Cascading Style Sheets**

- Neste projeto, você aprenderá o básico de CSS (Cascading Style Sheets) construindo um menu de café. ``CSS`` é a linguagem usada para estilizar um documento ``HTML``. Ela descreve como os elementos ``HTML`` devem ser exibidos na tela.

- Como você aprendeu nas últimas etapas do `**Cat Photo App**`, há uma estrutura básica necessária para começar a construir sua página da web. 

> Cada documento HTML deve ter uma declaração DOCTYPE e um elemento ``html``. O DOCTYPE informa ao navegador em qual versão do `HTML` o documento está. E o elemento `html` representa o elemento raiz que contém todos os outros elementos.

```html
<!DOCTYPE html>
<html lang="en">
<!--all other elements go here-->
</html>
```

- O título é um dos vários elementos que fornecem informações extras __não visíveis na página da web__, mas é útil para mecanismos de busca ou como a página é exibida.

- Dentro do elemento `head`, aninhe um metaelemento com um atributo chamado charset definido para o valor `utf-8` para informar ao navegador como codificar caracteres para a página.

> Até agora, você tem sido limitado quanto à apresentação e aparência do conteúdo que cria. Para começar a assumir o **controle**, adicione um elemento de `style` dentro do elemento `head`.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>Cafe Menu</title>
    <style></style>
  </head>
  <body>
    <main>
      <h1>CAMPER CAFE</h1>
      <p>Est. 2020</p>
      <section>
        <h2>Coffee</h2>
      </section>
    </main>
  </body>
</html>
```
- Você pode adicionar estilo a um elemento especificando-o no elemento style e definindo uma propriedade para ele como esta:

```html
<style>
    element {
 property: value;
}
</style>
```

- Na etapa anterior, você usou um seletor de tipo para estilizar o elemento `h1`. Centralize o conteúdo dos elementos `h2` e `p` adicionando um novo seletor de tipo para cada um deles ao elemento de estilo existente.

```html
<style>
    h1 {
    text-align: center;
    }
    h2 {
    text-align: center;
    }
    p {
    text-align: center;
    }
</style>
```

- Agora você tem três seletores de tipo com o mesmo estilo exato. Você pode adicionar o mesmo grupo de estilos a muitos elementos criando uma lista de seletores. Cada seletor é separado por vírgulas como esta:

```html
<style>
    selector1, selector2 {
    property: value;
    }
</style>
```

> Você estilizou três elementos escrevendo CSS dentro das tags de estilo. Isso funciona, mas como haverá muito mais estilos, é melhor colocar todos os estilos em um arquivo separado e vincular a ele.

- Criamos um arquivo styles.css separado para você e trocamos a visualização do editor para esse arquivo. Você pode alternar entre os arquivos com as guias na parte superior do editor.

- Comece reescrevendo os estilos que você criou no arquivo styles.css. Certifique-se de excluir as tags de estilo de abertura e fechamento.

```css
h1, h2, p {
    text-align: center;
}
```

- Agora que você tem o `CSS` no arquivo `styles.css`, vá em frente e remova o elemento `style` e todo o seu conteúdo. Uma vez removido, o texto que estava centralizado irá mudar de volta para a esquerda.

> Agora você precisa vincular o arquivo `styles.css`, para que os estilos sejam aplicados novamente. Dentro do elemento head, adicione um elemento `link`. Dê a ele um atributo `rel` com o valor de `"stylesheet"` e um atributo `href` com o valor de `"styles.css"`.

---

> Para que o estilo da página pareça similar no celular como em um *desktop* ou *laptop*, você precisa adicionar um metaelemento com um atributo `content` especial.

Adicione o seguinte dentro do elemento `head`:

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
```

### Elemnto `DIV`

> O elemento `div` é usado principalmente para propósitos de **layout de design**, diferentemente dos outros elementos de conteúdo que você usou até agora.

Ex.:

```html
<body>
    <div id="menu">
        <main>
            <h1>CAMPER CAFE</h1>
            <p>Est. 2020</p>
            <section>
                <h2>Coffee</h2>
            </section>
        </main>
    </div>
</body>
```

- O objetivo agora é fazer com que o `div` não ocupe toda a largura da página. A propriedade `width` do `CSS` é perfeita para isso.

- Você pode usar o seletor `id` para direcionar um elemento específico com um atributo `id`. Um seletor `id` é definido colocando o símbolo **hash** `#` diretamente na frente do valor `id` do elemento. 
    
    - Por exemplo, se um elemento tem o `id` de **"cat"**, então você direcionaria esse elemento assim:

    ```css
    #cat {
      width: 250px;
    }
    ```

> Comentários em CSS:

```css
/* Seu comentário aqui */
```

- Agora é fácil ver que o texto está centralizado dentro do elemento `#menu`. Atualmente, a largura do elemento `#menu` é especificada em pixels (`px`).

- Altere o valor da propriedade `width` para `80%`, para torná-la `80%` da largura do seu elemento pai (`body`).

---

## class selector

- Até agora você tem usado seletores de `type` e `id` para estilizar elementos. No entanto, é mais comum usar um seletor diferente para estilizar seus elementos.

- Um seletor de classe | `class selector` | é definido por um nome com um ponto diretamente na frente dele, assim:

```css
.class-name {
  styles
}
```

- Para aplicar o estilo da **classe** ao elemento `div`, remova o **atributo** `id` e adicione um **atributo** `class` à **tag de abertura** do elemento `div`. Certifique-se de definir o valor `class` como **menu**.

```html
<div class="menu">
```

> Parece bom. Hora de começar a adicionar alguns itens de menu. Adicione um elemento de artigo `article` vazio sob o título Café. Ele conterá um sabor e preço de cada café que você oferece atualmente.

- Elementos de artigo `article` geralmente contêm vários elementos que têm informações relacionadas. Neste caso, ele conterá um sabor de café e um preço para esse sabor. Aninhe dois elementos `p` dentro do seu elemento de artigo. O texto do primeiro deve ser French Vanilla, e o texto do segundo, 3.00.

---

- É mais ou menos isso que você quer, mas agora seria legal se o sabor e o preço estivessem na mesma linha. 

- Os elementos `p` são elementos de nível de bloco `block-level`, então eles ocupam toda a largura do elemento pai.

- Para colocá-los na mesma linha, você precisa aplicar algum estilo aos elementos `p` para que eles se comportem mais como elementos `inline`. Para fazer isso, comece adicionando um atributo `class` com o valor `item` ao primeiro elemento **article** sob o título Coffee.

> Os elementos `p` são aninhados em um elemento `article` com o atributo `class` de **"item"**. Você pode estilizar todos os elementos `p` aninhados em qualquer lugar em elementos com uma **classe** chamada `item` assim:

```css
.item p { }
```

```
That's closer, but the price didn't stay over on the right. This is because `inline-block` elements only take up the `width` of their content. To spread them out, add a `width` *property* to the `flavor` and `price` **class selectors** that have a value of `50%` each.
```

- Isso é mais próximo, mas o preço não ficou mais à direita. Isso ocorre porque os elementos inline-block ocupam apenas a largura do seu conteúdo. Para espalhá-los, adicione uma propriedade width aos seletores de classe flavor e price que têm um valor de 50% cada.

- Bem, isso não funcionou. Estilizar os elementos `p` como `inline-block` e colocá-los em linhas separadas no código cria um espaço extra à direita do primeiro elemento `p`, fazendo com que o segundo mude para a próxima linha. Caracteres de espaço em branco também podem causar esse problema.

- Uma maneira de corrigir isso é tornar a largura de cada elemento `p` um pouco menor que `50%`. Altere o valor da largura `width` para `49%` para cada classe para ver o que acontece.

- Isso funcionou, mas ainda há um pequeno espaço à direita do preço.

- Você pode continuar tentando várias porcentagens para as larguras. Em vez disso, use a tecla back space no seu teclado para mover o elemento p com a classe price ao lado do elemento p com a classe flavor para que eles fiquem na mesma linha no editor. Certifique-se de que não haja espaço entre os dois elementos.

- Agora vá em frente e altere as larguras das classes de sabor e preço para 50% novamente.

> Se você diminuir a largura da pré-visualização da página, notará que em algum momento parte do texto à esquerda começa a se ajustar à próxima linha. Isso ocorre porque a largura dos elementos p no lado esquerdo só pode ocupar 50% do espaço.

- Como você sabe que os preços à direita têm significativamente menos caracteres, altere o valor da largura da classe de sabor para 75% e o valor da largura da classe de preço para 25%.

