# Avaliação 3 de Análise e desenvolvimento de sistemas - Descrição.

## Introdução

O projeto de Análise e Desenvolvimento de Sistemas tem como objetivo desenvolver um sistema de gestão escolar para facilitar o controle e administração das atividades acadêmicas de uma escola. O sistema será responsável por gerenciar informações de alunos, disciplinas, professores, notas, frequência e demais aspectos relacionados ao ambiente escolar.

## Objetivos

O principal objetivo do projeto é criar um sistema eficiente e intuitivo que permita o registro, consulta e atualização de dados acadêmicos, proporcionando uma melhor organização e agilidade no processo de gestão escolar. Alguns objetivos específicos incluem:

- Cadastro e manutenção de informações de alunos, como nome, matrícula, dados pessoais, etc.
- Registro de notas e frequência dos alunos em cada disciplina.
- Geração de relatórios e estatísticas para auxiliar na tomada de decisões da equipe gestora.
- Controle de acesso e permissões de usuários, garantindo a segurança e privacidade das informações.
# Arquitetura do Projeto

## Front-end
O front-end do projeto é desenvolvido utilizando o Streamlit, uma biblioteca em Python para construção de interfaces web. O Streamlit permite criar páginas interativas e exibir informações ao usuário, como formulários, tabelas e gráficos.

## Back-end
O back-end do projeto é implementado utilizando o MongoDB como banco de dados e o PyMongo como driver de conexão com o MongoDB. O PyMongo é uma biblioteca em Python que permite interagir com o banco de dados MongoDB, executando operações como inserção, consulta e atualização de documentos.

## Estrutura do projeto
O projeto é dividido em páginas, cada uma responsável por uma funcionalidade específica. Por exemplo, há uma página para cadastrar alunos, uma página para cadastrar disciplinas, uma página para registrar a presença dos alunos, etc. Cada página é implementada em um arquivo separado e importada no arquivo principal do projeto.

## Conexão com o banco de dados
A conexão com o banco de dados MongoDB é estabelecida utilizando o MongoClient do PyMongo. O MongoClient permite estabelecer uma conexão com o banco de dados especificando a URL de conexão e o nome do banco de dados.

## Operações no banco de dados
Para realizar operações no banco de dados, como inserção, consulta e atualização de documentos, são utilizados os métodos disponibilizados pelo PyMongo. Por exemplo, para inserir um documento na coleção de alunos, é utilizado o método insert_one().

## Interação com o usuário
O Streamlit é utilizado para exibir formulários e interagir com o usuário. O usuário pode preencher os campos nos formulários, selecionar opções, e clicar em botões para executar ações, como cadastrar um aluno, cadastrar uma disciplina, etc.

## Tratamento de erros
O projeto deve incluir tratamento de erros para lidar com situações como campos vazios, valores inválidos, falhas na conexão com o banco de dados, etc. Mensagens de erro apropriadas devem ser exibidas ao usuário para fornecer feedback sobre o ocorrido.

Essa é uma visão geral da arquitetura lógica do projeto, mostrando como os diferentes componentes se integram para fornecer as funcionalidades desejadas. É importante ressaltar que a arquitetura pode ser adaptada de acordo com as necessidades específicas do projeto.
