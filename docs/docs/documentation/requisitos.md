<div align="justify"> Este documento descreve os requisitos do sistema são divididos em <strong> funcionais </strong> e <strong>não funcionais</strong>, conforme descrito abaixo.</div>

## Requisitos Funcionais

Os requisitos funcionais descrevem as funcionalidades específicas que o sistema deve oferecer para atender às necessidades do usuário ou ao propósito do software.

| Número | Requisito                                                                                             |
|--------|-------------------------------------------------------------------------------------------------------|
| RF01   | O dashboard deve mostrar de forma visual (gráficos/tabelas) o resultado da análise, auxiliando assim o usuário na tomada de decisão.         |
| RF02   | O dashboard deve atualizar os dados diariamente, para garantir a atualização das informações.                                              |
| RF03   | O dashboard deve conter filtros para personalização de dados e visualização de acordo com suas necessidades, como tempo e sentimento.      |
| RF04   | O dashboard deve ter elementos gráficos interativos.                                                                                       |
| RF05   | O sistema deve integrar-se com a fonte de dados do projeto automaticamente, para extração de dados.                                                                  |
| RF06   | O sistema deve identificar se os sentimentos relacionados a um tópico são positivos, negativos ou neutros.                                  |
| RF07   | O sistema deve classificar os dados em categorias predefinidas, como contributivas ou irrelevantes.                                         |
| RF08   | O sistema deve exibir os resultados da análise de sentimentos em gráficos claros e interativos.                                            |
| RF09   | O sistema deve conter DAGs configuradas no Airflow para coleta, processamento e armazenamento de dados.                                     |
| RF10   | O sistema deve armazenar os dados processados em um banco de dados PostgreSQL.                                                              |

---

## Requisitos Não Funcionais

Os requisitos não funcionais descrevem características de qualidade do sistema, como desempenho, usabilidade, segurança, e outras restrições relacionadas ao ambiente ou à arquitetura.

| Número | Requisito                                                                                             |
|--------|-------------------------------------------------------------------------------------------------------|
| RNF01  | A interface do dashboard deve ser responsiva e adaptar-se a diferentes dispositivos (desktop, tablet, mobile).                              |
| RNF02  | O dashboard deve ter uma interface fácil de navegar, com elementos bem organizados e uma hierarquia visual clara, incluindo menus e links.  |
| RNF03  | O dashboard deve ter uma identidade visual agradável.                                                                                      |
| RNF04  | O dashboard precisa estar disponível 24 horas por dia.                                                                                     |
| RNF05  | O dashboard precisa ser acessado na página designada.                                                                                      |
| RNF06  | O dashboard deve funcionar nos principais navegadores: Safari, Firefox, Chrome.                                                            |
| RNF07  | O dashboard deve poder ser acessado no computador (WEB).                                                                                   |
| RNF08  | O código deve ser bem documentado e estruturado para facilitar futuras manutenções e permitir a adição de novas funcionalidades sem impacto negativo nas existentes. |
| RNF09  | A infraestrutura deve suportar o aumento do volume de dados sem comprometer o desempenho.                                                  |
| RNF10  | O sistema deve garantir uma disponibilidade mínima de 90% ao longo do mês.                                                               |
| RNF11  | A interface do sistema deve ser intuitiva, permitindo que um novo usuário compreenda seu funcionamento sem treinamento adicional.            |
| RNF12  | O sistema deve ser conteinerizado para facilitar implantação em diferentes ambientes.                                                       |
| RNF13  | O sistema deve atender às regulamentações de proteção de dados, como a LGPD.                                                                |

---

Tabela de Versionamento

| Versão | Data       | Descrição                                                     | Autor(es)        |
|--------|------------|---------------------------------------------------------------|------------------|
| 1.0    | 28/11/2024 | Criação inicial                       | Gabriel Pinto |
| 1.1    | 01/12/2024 | Estruturação e atualização            | Gabriel Pinto |
| 1.2    | 11/12/2024 | Atualização                           | Gabriel Pinto |