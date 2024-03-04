<!DOCTYPE html>
<html>
<head>
<title>Exemplo de PHP com HTML pt.2</title>
</head>
<body>

<?php
$nome = "Maria";
$saudacao = "Bem-vinda, " . $nome . "!";
echo $saudacao; // Saída: Bem-vinda, Maria!?>
<br>

<?php 
$produto = "óculos";
$preco = 100;
$mensagem = "O preço do " . $produto . " é R$" . $preco . ",00.";
echo $mensagem; // Saída: O preço do óculos é R$100,00.?>
<br>

<?php 
$primeiraParte = "obrigado, ";
$segundaParte = "por comprar!";
$saudacao = $primeiraParte . $segundaParte;
echo $saudacao; // Saída: obrigado por comprar!?>
<br> 

<?php
$mensagem = "Você tem ";
$mensagem .= "uma nova mensagem.";
echo $mensagem; // Saída: Você tem uma nova mensagem.
?>

</body>
</html>
