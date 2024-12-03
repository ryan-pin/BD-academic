[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/f63fFlqO)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=17331782)

# Prestador de serviço - Personal

## Tecnologias Utilizadas
- **Django**, **DjangoRest**, **Swagger** e **Postgres (PgAdmin)**

## Classes utilizadas

### Cliente
   - nome - string
   - telefone - string
   - social_midia - string
   - endereço - string
   - indicação - foreingkey(cliente)
    
### Serviço
   - descrição - string
   - valor - float
   - data-cadastro - dateTime
   - cliente - foreignkey(cliente)
   - pago - boolean
   - aberto - boolean

#### A classe serviço possui uma relação com cliente, possuindo um cliente

