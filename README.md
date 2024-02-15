# Automata Learning Routine for Auto-Twin

## Description

Module developed within the [Auto-Twin](https://www.auto-twin-project.eu/) Horizon EU project perform an automata
learning experiment with data
extracted from a System Knowledge Graph (SKG), store the resulting model in the SKG, and create semantic links between
the learned features and the existing nodes representing the system.

Authors:

| Name           | E-mail address           |
|:---------------|:-------------------------|
| Lestingi Livia | livia.lestingi@polimi.it |

## Requirements

Dependencies are listed in the [`environment.yml`](environment.yml) file.

## Module Structure

This module acts as an orchestrator of the following submodules:

- [`lsha`][lsha]: Automata learning component, specifically implementing algorithm L*_SHA for Stochastic
  Hybrid Automata (SHA) learning;
- [`skg_connector`][connector]: Component performing queries on the SKG to extract data and store the
  newly created model;
- [`sha2dt_semantic_mapper`][mapper]: Component identifying the semantic links between learned features and the existing
  representation of the System Under Learning (e.g., between an edge of the learned automaton and the sensor that
  triggers it).

Upon cloning the repository, run the following commands to initialize the submodules:

	git submodule init	
    git submodule update

Note that it is necessary to run `git submodule update` to synchronize the submodules with the corresponding
repositories.

## Configuration

The configuration file for the `skg_connector`
module [`config.ini`](submodules/skg_connector/resources/config/config.ini), by default, is set up as follows:

- **instance**: name of the .ini file containing the information necessary to connect to the SKG (mainly URI, user, and
  password). By default, this points to the [`local.ini`](submodules/skg_connector/resources/config/local.ini) file
  pointing to a local Neo4j instance with password `12345678`. Should a connection to a connection to a differently
  parameterized instance be needed, a new file with the same structure
  as [`local.ini`](submodules/skg_connector/resources/config/local.ini) must be added in the same folder, and parameter
  **instance** updated to the new name.
- **schema.name**: identifier of the use case targeted by the automata learning experiment. By default, this is set
  to [`legoFactory`](submodules/skg_connector/resources/schemas/legoFactory.json), but it can be changed to any value
  from the [`schema`](submodules/skg_connector/resources/schemas) folder.

---

*Copyright &copy; 2024 Livia Lestingi*

[lsha]: https://github.com/LesLivia/lsha/tree/master

[connector]: https://github.com/LesLivia/skg_connector

[mapper]: https://github.com/LesLivia/sha2dt_semantic_mapper
