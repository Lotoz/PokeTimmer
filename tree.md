📦Poketimmer
 ┣ 📂api
 ┃ ┣ 📂management
 ┃ ┃ ┗ 📂commands
 ┃ ┃ ┃ ┗ 📜cargar_kanto.py
 ┃ ┣ 📂migrations
 ┃ ┃ ┣ 📜0001_initial.py
 ┃ ┃ ┣ 📜0002_alter_pokedexentry_sprite_url.py
 ┃ ┃ ┣ 📜0003_pokedexentry_evolucion_siguiente_and_more.py
 ┃ ┃ ┣ 📜0004_pokedexentry_tipo_secundario.py
 ┃ ┃ ┗ 📜0005_pokedexentry_sprite_shiny_url_and_more.py
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜serializers.py
 ┃ ┣ 📜urls.py
 ┃ ┗ 📜views.py
 ┣ 📂backend
 ┃ ┣ 📜asgi.py
 ┃ ┣ 📜settings.py
 ┃ ┣ 📜urls.py
 ┃ ┗ 📜wsgi.py
 ┣ 📂frontend
 ┃ ┣ 📂electron
 ┃ ┃ ┗ 📜main.cjs
 ┃ ┣ 📂public
 ┃ ┃ ┗ 📜vite.svg
 ┃ ┣ 📂src
 ┃ ┃ ┣ 📂api
 ┃ ┃ ┃ ┗ 📜axios.js
 ┃ ┃ ┣ 📂assets
 ┃ ┃ ┃ ┗ 📜vue.svg
 ┃ ┃ ┣ 📂components
 ┃ ┃ ┃ ┣ 📜EquipoPokemon.vue
 ┃ ┃ ┃ ┣ 📜ListaTareas.vue
 ┃ ┃ ┃ ┗ 📜PomodoroTimer.vue
 ┃ ┃ ┣ 📂utils
 ┃ ┃ ┃ ┗ 📜prettyAlert.js
 ┃ ┃ ┣ 📂views
 ┃ ┃ ┃ ┣ 📜DashboardView.vue
 ┃ ┃ ┃ ┣ 📜LoginView.vue
 ┃ ┃ ┃ ┣ 📜PCView.vue
 ┃ ┃ ┃ ┣ 📜PokedexView.vue
 ┃ ┃ ┃ ┣ 📜ProfileView.vue
 ┃ ┃ ┃ ┗ 📜RegistroView.vue
 ┃ ┃ ┣ 📜App.vue
 ┃ ┃ ┣ 📜main.js
 ┃ ┃ ┣ 📜router.js
 ┃ ┃ ┗ 📜style.css
 ┃ ┣ 📜index.html
 ┃ ┣ 📜package.json
 ┃ ┗ 📜vite.config.js
 ┣ 📂media
 ┃ ┗ 📂pokemon
 ┃ ┃ ┣ 📂normal
 ┃ ┃ ┃ ┗ 📜 ... (151 pokemon images)
 ┃ ┃ ┣ 📂shiny
 ┃ ┃ ┃ ┗ 📜 ... (151 shiny pokemon images)
 ┃ ┃ ┗ 📜alola.jpg
 ┣ 📜.env.example
 ┣ 📜db.sqlite3
 ┣ 📜download_sprites.py
 ┣ 📜generar_pokedex.py
 ┣ 📜manage.py
 ┣ 📜pokedex.json
 ┗ 📜requirements.txt
 ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┣ 📜index.d.ts
 ┃ ┃ ┃ ┣ 📜index.js
 ┃ ┃ ┃ ┣ 📜package.json
 ┃ ┃ ┃ ┣ 📜shams.d.ts
 ┃ ┃ ┃ ┣ 📜shams.js
 ┃ ┃ ┃ ┗ 📜tsconfig.json
 ┃ ┃ ┣ 📂hasown
 ┃ ┃ ┃ ┣ 📂.github
 ┃ ┃ ┃ ┃ ┗ 📜FUNDING.yml
 ┃ ┃ ┃ ┣ 📜.eslintrc
 ┃ ┃ ┃ ┣ 📜.nycrc
 ┃ ┃ ┃ ┣ 📜CHANGELOG.md
 ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┣ 📜index.d.ts
 ┃ ┃ ┃ ┣ 📜index.js
 ┃ ┃ ┃ ┣ 📜package.json
 ┃ ┃ ┃ ┗ 📜tsconfig.json
 ┃ ┃ ┣ 📂hookable
 ┃ ┃ ┃ ┣ 📂dist
 ┃ ┃ ┃ ┃ ┣ 📜index.cjs
 ┃ ┃ ┃ ┃ ┣ 📜index.d.ts
 ┃ ┃ ┃ ┃ ┗ 📜index.mjs
 ┃ ┃ ┃ ┣ 📜LICENSE.md
 ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┗ 📜package.json
 ┃ ┃ ┣ 📂http-cache-semantics
 ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┣ 📜index.js
 ┃ ┃ ┃ ┗ 📜package.json
 ┃ ┃ ┣ 📂http2-wrapper
 ┃ ┃ ┃ ┣ 📂source
 ┃ ┃ ┃ ┃ ┣ 📂utils
 ┃ ┃ ┃ ┃ ┃ ┣ 📜calculate-server-name.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📜errors.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📜is-request-pseudo-header.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📜proxy-events.js
 ┃ ┃ ┃ ┃ ┃ ┗ 📜url-to-options.js
 ┃ ┃ ┃ ┃ ┣ 📜agent.js
 ┃ ┃ ┃ ┃ ┣ 📜auto.js
 ┃ ┃ ┃ ┃ ┣ 📜client-request.js
 ┃ ┃ ┃ ┃ ┣ 📜incoming-message.js
 ┃ ┃ ┃ ┃ ┗ 📜index.js
 ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┗ 📜package.json
 ┃ ┃ ┣ 📂is-what
 ┃ ┃ ┃ ┣ 📂dist
 ┃ ┃ ┃ ┃ ┣ 📜getType.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜getType.js
 ┃ ┃ ┃ ┃ ┣ 📜index.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜index.js
 ┃ ┃ ┃ ┃ ┣ 📜isAnyObject.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜isAnyObject.js
 ┃ ┃ ┃ ┃ ┣ 📜isArray.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜isArray.js
 ┃ ┃ ┃ ┃ ┣ 📜isBigInt.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜isBigInt.js
 ┃ ┃ ┃ ┃ ┣ 📜isBlob.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜isBlob.js
 ┃ ┃ ┃ ┃ ┣ 📜isBoolean.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜isBoolean.js
 ┃ ┃ ┃ ┃ ┣ 📜isDate.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜isDate.js
 ┃ ┃ ┃ ┃ ┣ 📜isEmptyArray.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜isEmptyArray.js
 ┃ ┃ ┃ ┃ ┣ 📜isEmptyObject.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜isEmptyObject.js
 ┃ ┃ ┃ ┃ ┣ 📜isEmptyString.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜isEmptyString.js
 ┃ ┃ ┃ ┃ ┣ 📜isError.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜isError.js
 ┃ ┃ ┃ ┃ ┣ 📜isFile.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜isFile.js
 ┃ ┃ ┃ ┃ ┣ 📜isFullArray.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜isFullArray.js
 ┃ ┃ ┃ ┃ ┣ 📜isFullObject.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜isFullObject.js
 ┃ ┃ ┃ ┃ ┣ 📜isFullString.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜isFullString.js
 ┃ ┃ ┃ ┃ ┣ 📜isFunction.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜isFunction.js
 ┃ ┃ ┃ ┃ ┣ 📜isHexDecimal.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜isHexDecimal.js
 ┃ ┃ ┃ ┃ ┣ 📜isInstanceOf.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜isInstanceOf.js
 ┃ ┃ ┃ ┃ ┣ 📜isInteger.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜isInteger.js
 ┃ ┃ ┃ ┃ ┣ 📜isIterable.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜isIterable.js
 ┃ ┃ ┃ ┃ ┣ 📜isMap.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜isMap.js
 ┃ ┃ ┃ ┃ ┣ 📜isNaNValue.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜isNaNValue.js
 ┃ ┃ ┃ ┃ ┣ 📜isNegativeInteger.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜isNegativeInteger.js
 ┃ ┃ ┃ ┃ ┣ 📜isNegativeNumber.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜isNegativeNumber.js
 ┃ ┃ ┃ ┃ ┣ 📜isNull.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜isNull.js
 ┃ ┃ ┃ ┃ ┣ 📜isNullOrUndefined.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜isNullOrUndefined.js
 ┃ ┃ ┃ ┃ ┣ 📜isNumber.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜isNumber.js
 ┃ ┃ ┃ ┃ ┣ 📜isObject.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜isObject.js
 ┃ ┃ ┃ ┃ ┣ 📜isObjectLike.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜isObjectLike.js
 ┃ ┃ ┃ ┃ ┣ 📜isOneOf.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜isOneOf.js
 ┃ ┃ ┃ ┃ ┣ 📜isPlainObject.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜isPlainObject.js
 ┃ ┃ ┃ ┃ ┣ 📜isPositiveInteger.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜isPositiveInteger.js
 ┃ ┃ ┃ ┃ ┣ 📜isPositiveNumber.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜isPositiveNumber.js
 ┃ ┃ ┃ ┃ ┣ 📜isPrimitive.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜isPrimitive.js
 ┃ ┃ ┃ ┃ ┣ 📜isPromise.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜isPromise.js
 ┃ ┃ ┃ ┃ ┣ 📜isRegExp.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜isRegExp.js
 ┃ ┃ ┃ ┃ ┣ 📜isSet.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜isSet.js
 ┃ ┃ ┃ ┃ ┣ 📜isString.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜isString.js
 ┃ ┃ ┃ ┃ ┣ 📜isSymbol.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜isSymbol.js
 ┃ ┃ ┃ ┃ ┣ 📜isType.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜isType.js
 ┃ ┃ ┃ ┃ ┣ 📜isUndefined.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜isUndefined.js
 ┃ ┃ ┃ ┃ ┣ 📜isWeakMap.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜isWeakMap.js
 ┃ ┃ ┃ ┃ ┣ 📜isWeakSet.d.ts
 ┃ ┃ ┃ ┃ ┗ 📜isWeakSet.js
 ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┗ 📜package.json
 ┃ ┃ ┣ 📂jsesc
 ┃ ┃ ┃ ┣ 📂bin
 ┃ ┃ ┃ ┃ ┗ 📜jsesc
 ┃ ┃ ┃ ┣ 📂man
 ┃ ┃ ┃ ┃ ┗ 📜jsesc.1
 ┃ ┃ ┃ ┣ 📜LICENSE-MIT.txt
 ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┣ 📜jsesc.js
 ┃ ┃ ┃ ┗ 📜package.json
 ┃ ┃ ┣ 📂json-buffer
 ┃ ┃ ┃ ┣ 📂test
 ┃ ┃ ┃ ┃ ┗ 📜index.js
 ┃ ┃ ┃ ┣ 📜.travis.yml
 ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┣ 📜index.js
 ┃ ┃ ┃ ┗ 📜package.json
 ┃ ┃ ┣ 📂json-stringify-safe
 ┃ ┃ ┃ ┣ 📂test
 ┃ ┃ ┃ ┃ ┣ 📜mocha.opts
 ┃ ┃ ┃ ┃ ┗ 📜stringify_test.js
 ┃ ┃ ┃ ┣ 📜.npmignore
 ┃ ┃ ┃ ┣ 📜CHANGELOG.md
 ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┣ 📜Makefile
 ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┣ 📜package.json
 ┃ ┃ ┃ ┗ 📜stringify.js
 ┃ ┃ ┣ 📂json5
 ┃ ┃ ┃ ┣ 📂dist
 ┃ ┃ ┃ ┃ ┣ 📜index.js
 ┃ ┃ ┃ ┃ ┣ 📜index.min.js
 ┃ ┃ ┃ ┃ ┣ 📜index.min.mjs
 ┃ ┃ ┃ ┃ ┗ 📜index.mjs
 ┃ ┃ ┃ ┣ 📂lib
 ┃ ┃ ┃ ┃ ┣ 📜cli.js
 ┃ ┃ ┃ ┃ ┣ 📜index.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜index.js
 ┃ ┃ ┃ ┃ ┣ 📜parse.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜parse.js
 ┃ ┃ ┃ ┃ ┣ 📜register.js
 ┃ ┃ ┃ ┃ ┣ 📜require.js
 ┃ ┃ ┃ ┃ ┣ 📜stringify.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜stringify.js
 ┃ ┃ ┃ ┃ ┣ 📜unicode.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜unicode.js
 ┃ ┃ ┃ ┃ ┣ 📜util.d.ts
 ┃ ┃ ┃ ┃ ┗ 📜util.js
 ┃ ┃ ┃ ┣ 📜LICENSE.md
 ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┗ 📜package.json
 ┃ ┃ ┣ 📂jsonfile
 ┃ ┃ ┃ ┣ 📜CHANGELOG.md
 ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┣ 📜index.js
 ┃ ┃ ┃ ┗ 📜package.json
 ┃ ┃ ┣ 📂keyv
 ┃ ┃ ┃ ┣ 📂src
 ┃ ┃ ┃ ┃ ┣ 📜index.d.ts
 ┃ ┃ ┃ ┃ ┗ 📜index.js
 ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┗ 📜package.json
 ┃ ┃ ┣ 📂local-pkg
 ┃ ┃ ┃ ┣ 📂dist
 ┃ ┃ ┃ ┃ ┣ 📜index.cjs
 ┃ ┃ ┃ ┃ ┣ 📜index.d.cts
 ┃ ┃ ┃ ┃ ┣ 📜index.d.mts
 ┃ ┃ ┃ ┃ ┣ 📜index.d.ts
 ┃ ┃ ┃ ┃ ┗ 📜index.mjs
 ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┗ 📜package.json
 ┃ ┃ ┣ 📂lowercase-keys
 ┃ ┃ ┃ ┣ 📜index.d.ts
 ┃ ┃ ┃ ┣ 📜index.js
 ┃ ┃ ┃ ┣ 📜license
 ┃ ┃ ┃ ┣ 📜package.json
 ┃ ┃ ┃ ┗ 📜readme.md
 ┃ ┃ ┣ 📂magic-string
 ┃ ┃ ┃ ┣ 📂dist
 ┃ ┃ ┃ ┃ ┣ 📜magic-string.cjs.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜magic-string.cjs.js
 ┃ ┃ ┃ ┃ ┣ 📜magic-string.cjs.js.map
 ┃ ┃ ┃ ┃ ┣ 📜magic-string.es.d.mts
 ┃ ┃ ┃ ┃ ┣ 📜magic-string.es.mjs
 ┃ ┃ ┃ ┃ ┣ 📜magic-string.es.mjs.map
 ┃ ┃ ┃ ┃ ┣ 📜magic-string.umd.js
 ┃ ┃ ┃ ┃ ┗ 📜magic-string.umd.js.map
 ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┗ 📜package.json
 ┃ ┃ ┣ 📂magic-string-ast
 ┃ ┃ ┃ ┣ 📂dist
 ┃ ┃ ┃ ┃ ┣ 📜index.d.ts
 ┃ ┃ ┃ ┃ ┗ 📜index.js
 ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┗ 📜package.json
 ┃ ┃ ┣ 📂matcher
 ┃ ┃ ┃ ┣ 📜index.d.ts
 ┃ ┃ ┃ ┣ 📜index.js
 ┃ ┃ ┃ ┣ 📜license
 ┃ ┃ ┃ ┣ 📜package.json
 ┃ ┃ ┃ ┗ 📜readme.md
 ┃ ┃ ┣ 📂math-intrinsics
 ┃ ┃ ┃ ┣ 📂.github
 ┃ ┃ ┃ ┃ ┗ 📜FUNDING.yml
 ┃ ┃ ┃ ┣ 📂constants
 ┃ ┃ ┃ ┃ ┣ 📜maxArrayLength.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜maxArrayLength.js
 ┃ ┃ ┃ ┃ ┣ 📜maxSafeInteger.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜maxSafeInteger.js
 ┃ ┃ ┃ ┃ ┣ 📜maxValue.d.ts
 ┃ ┃ ┃ ┃ ┗ 📜maxValue.js
 ┃ ┃ ┃ ┣ 📂test
 ┃ ┃ ┃ ┃ ┗ 📜index.js
 ┃ ┃ ┃ ┣ 📜.eslintrc
 ┃ ┃ ┃ ┣ 📜CHANGELOG.md
 ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┣ 📜abs.d.ts
 ┃ ┃ ┃ ┣ 📜abs.js
 ┃ ┃ ┃ ┣ 📜floor.d.ts
 ┃ ┃ ┃ ┣ 📜floor.js
 ┃ ┃ ┃ ┣ 📜isFinite.d.ts
 ┃ ┃ ┃ ┣ 📜isFinite.js
 ┃ ┃ ┃ ┣ 📜isInteger.d.ts
 ┃ ┃ ┃ ┣ 📜isInteger.js
 ┃ ┃ ┃ ┣ 📜isNaN.d.ts
 ┃ ┃ ┃ ┣ 📜isNaN.js
 ┃ ┃ ┃ ┣ 📜isNegativeZero.d.ts
 ┃ ┃ ┃ ┣ 📜isNegativeZero.js
 ┃ ┃ ┃ ┣ 📜max.d.ts
 ┃ ┃ ┃ ┣ 📜max.js
 ┃ ┃ ┃ ┣ 📜min.d.ts
 ┃ ┃ ┃ ┣ 📜min.js
 ┃ ┃ ┃ ┣ 📜mod.d.ts
 ┃ ┃ ┃ ┣ 📜mod.js
 ┃ ┃ ┃ ┣ 📜package.json
 ┃ ┃ ┃ ┣ 📜pow.d.ts
 ┃ ┃ ┃ ┣ 📜pow.js
 ┃ ┃ ┃ ┣ 📜round.d.ts
 ┃ ┃ ┃ ┣ 📜round.js
 ┃ ┃ ┃ ┣ 📜sign.d.ts
 ┃ ┃ ┃ ┣ 📜sign.js
 ┃ ┃ ┃ ┗ 📜tsconfig.json
 ┃ ┃ ┣ 📂mime-db
 ┃ ┃ ┃ ┣ 📜HISTORY.md
 ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┣ 📜db.json
 ┃ ┃ ┃ ┣ 📜index.js
 ┃ ┃ ┃ ┗ 📜package.json
 ┃ ┃ ┣ 📂mime-types
 ┃ ┃ ┃ ┣ 📜HISTORY.md
 ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┣ 📜index.js
 ┃ ┃ ┃ ┗ 📜package.json
 ┃ ┃ ┣ 📂mimic-response
 ┃ ┃ ┃ ┣ 📜index.js
 ┃ ┃ ┃ ┣ 📜license
 ┃ ┃ ┃ ┣ 📜package.json
 ┃ ┃ ┃ ┗ 📜readme.md
 ┃ ┃ ┣ 📂mitt
 ┃ ┃ ┃ ┣ 📂dist
 ┃ ┃ ┃ ┃ ┣ 📜mitt.js
 ┃ ┃ ┃ ┃ ┣ 📜mitt.js.map
 ┃ ┃ ┃ ┃ ┣ 📜mitt.mjs
 ┃ ┃ ┃ ┃ ┣ 📜mitt.mjs.map
 ┃ ┃ ┃ ┃ ┣ 📜mitt.umd.js
 ┃ ┃ ┃ ┃ ┗ 📜mitt.umd.js.map
 ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┣ 📜index.d.ts
 ┃ ┃ ┃ ┗ 📜package.json
 ┃ ┃ ┣ 📂mlly
 ┃ ┃ ┃ ┣ 📂dist
 ┃ ┃ ┃ ┃ ┣ 📜index.cjs
 ┃ ┃ ┃ ┃ ┣ 📜index.d.cts
 ┃ ┃ ┃ ┃ ┣ 📜index.d.mts
 ┃ ┃ ┃ ┃ ┣ 📜index.d.ts
 ┃ ┃ ┃ ┃ ┗ 📜index.mjs
 ┃ ┃ ┃ ┣ 📂node_modules
 ┃ ┃ ┃ ┃ ┣ 📂confbox
 ┃ ┃ ┃ ┃ ┃ ┣ 📂dist
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂shared
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜confbox.3768c7e9.cjs
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜confbox.6b479c78.cjs
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜confbox.9388d834.mjs
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜confbox.9745c98f.d.cts
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜confbox.9745c98f.d.mts
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜confbox.9745c98f.d.ts
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜confbox.f9f03f05.mjs
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜index.cjs
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜index.d.cts
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜index.d.mts
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜index.d.ts
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜index.mjs
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜json5.cjs
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜json5.d.cts
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜json5.d.mts
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜json5.d.ts
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜json5.mjs
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜jsonc.cjs
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜jsonc.d.cts
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜jsonc.d.mts
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜jsonc.d.ts
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜jsonc.mjs
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜toml.cjs
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜toml.d.cts
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜toml.d.mts
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜toml.d.ts
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜toml.mjs
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜yaml.cjs
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜yaml.d.cts
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜yaml.d.mts
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜yaml.d.ts
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜yaml.mjs
 ┃ ┃ ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┃ ┃ ┣ 📜json5.d.ts
 ┃ ┃ ┃ ┃ ┃ ┣ 📜jsonc.d.ts
 ┃ ┃ ┃ ┃ ┃ ┣ 📜package.json
 ┃ ┃ ┃ ┃ ┃ ┣ 📜toml.d.ts
 ┃ ┃ ┃ ┃ ┃ ┗ 📜yaml.d.ts
 ┃ ┃ ┃ ┃ ┗ 📂pkg-types
 ┃ ┃ ┃ ┃ ┃ ┣ 📂dist
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜index.cjs
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜index.d.cts
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜index.d.mts
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜index.d.ts
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜index.mjs
 ┃ ┃ ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┃ ┃ ┗ 📜package.json
 ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┗ 📜package.json
 ┃ ┃ ┣ 📂ms
 ┃ ┃ ┃ ┣ 📜index.js
 ┃ ┃ ┃ ┣ 📜license.md
 ┃ ┃ ┃ ┣ 📜package.json
 ┃ ┃ ┃ ┗ 📜readme.md
 ┃ ┃ ┣ 📂muggle-string
 ┃ ┃ ┃ ┣ 📂out
 ┃ ┃ ┃ ┃ ┣ 📜base.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜base.js
 ┃ ┃ ┃ ┃ ┣ 📜basic.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜basic.js
 ┃ ┃ ┃ ┃ ┣ 📜binarySearch.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜binarySearch.js
 ┃ ┃ ┃ ┃ ┣ 📜common.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜common.js
 ┃ ┃ ┃ ┃ ┣ 📜getLength.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜getLength.js
 ┃ ┃ ┃ ┃ ┣ 📜index.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜index.js
 ┃ ┃ ┃ ┃ ┣ 📜map.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜map.js
 ┃ ┃ ┃ ┃ ┣ 📜overwriteSource.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜overwriteSource.js
 ┃ ┃ ┃ ┃ ┣ 📜replace.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜replace.js
 ┃ ┃ ┃ ┃ ┣ 📜segment.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜segment.js
 ┃ ┃ ┃ ┃ ┣ 📜sourceBased.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜sourceBased.js
 ┃ ┃ ┃ ┃ ┣ 📜toString.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜toString.js
 ┃ ┃ ┃ ┃ ┣ 📜track.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜track.js
 ┃ ┃ ┃ ┃ ┣ 📜types.d.ts
 ┃ ┃ ┃ ┃ ┗ 📜types.js
 ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┗ 📜package.json
 ┃ ┃ ┣ 📂nanoid
 ┃ ┃ ┃ ┣ 📂async
 ┃ ┃ ┃ ┃ ┣ 📜index.browser.cjs
 ┃ ┃ ┃ ┃ ┣ 📜index.browser.js
 ┃ ┃ ┃ ┃ ┣ 📜index.cjs
 ┃ ┃ ┃ ┃ ┣ 📜index.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜index.js
 ┃ ┃ ┃ ┃ ┣ 📜index.native.js
 ┃ ┃ ┃ ┃ ┗ 📜package.json
 ┃ ┃ ┃ ┣ 📂bin
 ┃ ┃ ┃ ┃ ┗ 📜nanoid.cjs
 ┃ ┃ ┃ ┣ 📂non-secure
 ┃ ┃ ┃ ┃ ┣ 📜index.cjs
 ┃ ┃ ┃ ┃ ┣ 📜index.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜index.js
 ┃ ┃ ┃ ┃ ┗ 📜package.json
 ┃ ┃ ┃ ┣ 📂url-alphabet
 ┃ ┃ ┃ ┃ ┣ 📜index.cjs
 ┃ ┃ ┃ ┃ ┣ 📜index.js
 ┃ ┃ ┃ ┃ ┗ 📜package.json
 ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┣ 📜index.browser.cjs
 ┃ ┃ ┃ ┣ 📜index.browser.js
 ┃ ┃ ┃ ┣ 📜index.cjs
 ┃ ┃ ┃ ┣ 📜index.d.cts
 ┃ ┃ ┃ ┣ 📜index.d.ts
 ┃ ┃ ┃ ┣ 📜index.js
 ┃ ┃ ┃ ┣ 📜nanoid.js
 ┃ ┃ ┃ ┗ 📜package.json
 ┃ ┃ ┣ 📂normalize-url
 ┃ ┃ ┃ ┣ 📜index.d.ts
 ┃ ┃ ┃ ┣ 📜index.js
 ┃ ┃ ┃ ┣ 📜license
 ┃ ┃ ┃ ┣ 📜package.json
 ┃ ┃ ┃ ┗ 📜readme.md
 ┃ ┃ ┣ 📂object-keys
 ┃ ┃ ┃ ┣ 📂test
 ┃ ┃ ┃ ┃ ┗ 📜index.js
 ┃ ┃ ┃ ┣ 📜.editorconfig
 ┃ ┃ ┃ ┣ 📜.eslintrc
 ┃ ┃ ┃ ┣ 📜.travis.yml
 ┃ ┃ ┃ ┣ 📜CHANGELOG.md
 ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┣ 📜implementation.js
 ┃ ┃ ┃ ┣ 📜index.js
 ┃ ┃ ┃ ┣ 📜isArguments.js
 ┃ ┃ ┃ ┗ 📜package.json
 ┃ ┃ ┣ 📂once
 ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┣ 📜once.js
 ┃ ┃ ┃ ┗ 📜package.json
 ┃ ┃ ┣ 📂p-cancelable
 ┃ ┃ ┃ ┣ 📜index.d.ts
 ┃ ┃ ┃ ┣ 📜index.js
 ┃ ┃ ┃ ┣ 📜license
 ┃ ┃ ┃ ┣ 📜package.json
 ┃ ┃ ┃ ┗ 📜readme.md
 ┃ ┃ ┣ 📂pathe
 ┃ ┃ ┃ ┣ 📂dist
 ┃ ┃ ┃ ┃ ┣ 📂shared
 ┃ ┃ ┃ ┃ ┃ ┣ 📜pathe.BSlhyZSM.cjs
 ┃ ┃ ┃ ┃ ┃ ┗ 📜pathe.M-eThtNZ.mjs
 ┃ ┃ ┃ ┃ ┣ 📜index.cjs
 ┃ ┃ ┃ ┃ ┣ 📜index.d.cts
 ┃ ┃ ┃ ┃ ┣ 📜index.d.mts
 ┃ ┃ ┃ ┃ ┣ 📜index.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜index.mjs
 ┃ ┃ ┃ ┃ ┣ 📜utils.cjs
 ┃ ┃ ┃ ┃ ┣ 📜utils.d.cts
 ┃ ┃ ┃ ┃ ┣ 📜utils.d.mts
 ┃ ┃ ┃ ┃ ┣ 📜utils.d.ts
 ┃ ┃ ┃ ┃ ┗ 📜utils.mjs
 ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┣ 📜package.json
 ┃ ┃ ┃ ┗ 📜utils.d.ts
 ┃ ┃ ┣ 📂pend
 ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┣ 📜index.js
 ┃ ┃ ┃ ┣ 📜package.json
 ┃ ┃ ┃ ┗ 📜test.js
 ┃ ┃ ┣ 📂perfect-debounce
 ┃ ┃ ┃ ┣ 📂dist
 ┃ ┃ ┃ ┃ ┣ 📜index.cjs
 ┃ ┃ ┃ ┃ ┣ 📜index.d.ts
 ┃ ┃ ┃ ┃ ┗ 📜index.mjs
 ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┗ 📜package.json
 ┃ ┃ ┣ 📂picocolors
 ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┣ 📜package.json
 ┃ ┃ ┃ ┣ 📜picocolors.browser.js
 ┃ ┃ ┃ ┣ 📜picocolors.d.ts
 ┃ ┃ ┃ ┣ 📜picocolors.js
 ┃ ┃ ┃ ┗ 📜types.d.ts
 ┃ ┃ ┣ 📂picomatch
 ┃ ┃ ┃ ┣ 📂lib
 ┃ ┃ ┃ ┃ ┣ 📜constants.js
 ┃ ┃ ┃ ┃ ┣ 📜parse.js
 ┃ ┃ ┃ ┃ ┣ 📜picomatch.js
 ┃ ┃ ┃ ┃ ┣ 📜scan.js
 ┃ ┃ ┃ ┃ ┗ 📜utils.js
 ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┣ 📜index.js
 ┃ ┃ ┃ ┣ 📜package.json
 ┃ ┃ ┃ ┗ 📜posix.js
 ┃ ┃ ┣ 📂pinia
 ┃ ┃ ┃ ┣ 📂dist
 ┃ ┃ ┃ ┃ ┣ 📜pinia.cjs
 ┃ ┃ ┃ ┃ ┣ 📜pinia.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜pinia.esm-browser.js
 ┃ ┃ ┃ ┃ ┣ 📜pinia.iife.js
 ┃ ┃ ┃ ┃ ┣ 📜pinia.iife.prod.js
 ┃ ┃ ┃ ┃ ┣ 📜pinia.mjs
 ┃ ┃ ┃ ┃ ┗ 📜pinia.prod.cjs
 ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┣ 📜index.cjs
 ┃ ┃ ┃ ┗ 📜package.json
 ┃ ┃ ┣ 📂pkg-types
 ┃ ┃ ┃ ┣ 📂dist
 ┃ ┃ ┃ ┃ ┣ 📜index.d.mts
 ┃ ┃ ┃ ┃ ┗ 📜index.mjs
 ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┗ 📜package.json
 ┃ ┃ ┣ 📂postcss
 ┃ ┃ ┃ ┣ 📂lib
 ┃ ┃ ┃ ┃ ┣ 📜at-rule.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜at-rule.js
 ┃ ┃ ┃ ┃ ┣ 📜comment.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜comment.js
 ┃ ┃ ┃ ┃ ┣ 📜container.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜container.js
 ┃ ┃ ┃ ┃ ┣ 📜css-syntax-error.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜css-syntax-error.js
 ┃ ┃ ┃ ┃ ┣ 📜declaration.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜declaration.js
 ┃ ┃ ┃ ┃ ┣ 📜document.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜document.js
 ┃ ┃ ┃ ┃ ┣ 📜fromJSON.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜fromJSON.js
 ┃ ┃ ┃ ┃ ┣ 📜input.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜input.js
 ┃ ┃ ┃ ┃ ┣ 📜lazy-result.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜lazy-result.js
 ┃ ┃ ┃ ┃ ┣ 📜list.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜list.js
 ┃ ┃ ┃ ┃ ┣ 📜map-generator.js
 ┃ ┃ ┃ ┃ ┣ 📜no-work-result.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜no-work-result.js
 ┃ ┃ ┃ ┃ ┣ 📜node.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜node.js
 ┃ ┃ ┃ ┃ ┣ 📜parse.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜parse.js
 ┃ ┃ ┃ ┃ ┣ 📜parser.js
 ┃ ┃ ┃ ┃ ┣ 📜postcss.d.mts
 ┃ ┃ ┃ ┃ ┣ 📜postcss.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜postcss.js
 ┃ ┃ ┃ ┃ ┣ 📜postcss.mjs
 ┃ ┃ ┃ ┃ ┣ 📜previous-map.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜previous-map.js
 ┃ ┃ ┃ ┃ ┣ 📜processor.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜processor.js
 ┃ ┃ ┃ ┃ ┣ 📜result.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜result.js
 ┃ ┃ ┃ ┃ ┣ 📜root.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜root.js
 ┃ ┃ ┃ ┃ ┣ 📜rule.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜rule.js
 ┃ ┃ ┃ ┃ ┣ 📜stringifier.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜stringifier.js
 ┃ ┃ ┃ ┃ ┣ 📜stringify.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜stringify.js
 ┃ ┃ ┃ ┃ ┣ 📜symbols.js
 ┃ ┃ ┃ ┃ ┣ 📜terminal-highlight.js
 ┃ ┃ ┃ ┃ ┣ 📜tokenize.js
 ┃ ┃ ┃ ┃ ┣ 📜warn-once.js
 ┃ ┃ ┃ ┃ ┣ 📜warning.d.ts
 ┃ ┃ ┃ ┃ ┗ 📜warning.js
 ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┗ 📜package.json
 ┃ ┃ ┣ 📂progress
 ┃ ┃ ┃ ┣ 📂lib
 ┃ ┃ ┃ ┃ ┗ 📜node-progress.js
 ┃ ┃ ┃ ┣ 📜CHANGELOG.md
 ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┣ 📜Makefile
 ┃ ┃ ┃ ┣ 📜Readme.md
 ┃ ┃ ┃ ┣ 📜index.js
 ┃ ┃ ┃ ┗ 📜package.json
 ┃ ┃ ┣ 📂proxy-from-env
 ┃ ┃ ┃ ┣ 📜.eslintrc
 ┃ ┃ ┃ ┣ 📜.travis.yml
 ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┣ 📜index.js
 ┃ ┃ ┃ ┣ 📜package.json
 ┃ ┃ ┃ ┗ 📜test.js
 ┃ ┃ ┣ 📂pump
 ┃ ┃ ┃ ┣ 📂.github
 ┃ ┃ ┃ ┃ ┗ 📜FUNDING.yml
 ┃ ┃ ┃ ┣ 📜.travis.yml
 ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┣ 📜SECURITY.md
 ┃ ┃ ┃ ┣ 📜index.js
 ┃ ┃ ┃ ┣ 📜package.json
 ┃ ┃ ┃ ┣ 📜test-browser.js
 ┃ ┃ ┃ ┗ 📜test-node.js
 ┃ ┃ ┣ 📂quansync
 ┃ ┃ ┃ ┣ 📂dist
 ┃ ┃ ┃ ┃ ┣ 📜index.cjs
 ┃ ┃ ┃ ┃ ┣ 📜index.d.cts
 ┃ ┃ ┃ ┃ ┣ 📜index.d.mts
 ┃ ┃ ┃ ┃ ┣ 📜index.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜index.mjs
 ┃ ┃ ┃ ┃ ┣ 📜macro.cjs
 ┃ ┃ ┃ ┃ ┣ 📜macro.d.cts
 ┃ ┃ ┃ ┃ ┣ 📜macro.d.mts
 ┃ ┃ ┃ ┃ ┣ 📜macro.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜macro.mjs
 ┃ ┃ ┃ ┃ ┣ 📜types.cjs
 ┃ ┃ ┃ ┃ ┣ 📜types.d.cts
 ┃ ┃ ┃ ┃ ┣ 📜types.d.mts
 ┃ ┃ ┃ ┃ ┣ 📜types.d.ts
 ┃ ┃ ┃ ┃ ┗ 📜types.mjs
 ┃ ┃ ┃ ┣ 📜LICENSE.md
 ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┗ 📜package.json
 ┃ ┃ ┣ 📂quick-lru
 ┃ ┃ ┃ ┣ 📜index.d.ts
 ┃ ┃ ┃ ┣ 📜index.js
 ┃ ┃ ┃ ┣ 📜license
 ┃ ┃ ┃ ┣ 📜package.json
 ┃ ┃ ┃ ┗ 📜readme.md
 ┃ ┃ ┣ 📂readdirp
 ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┣ 📜index.d.ts
 ┃ ┃ ┃ ┣ 📜index.js
 ┃ ┃ ┃ ┗ 📜package.json
 ┃ ┃ ┣ 📂resolve-alpn
 ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┣ 📜index.js
 ┃ ┃ ┃ ┗ 📜package.json
 ┃ ┃ ┣ 📂responselike
 ┃ ┃ ┃ ┣ 📂src
 ┃ ┃ ┃ ┃ ┗ 📜index.js
 ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┗ 📜package.json
 ┃ ┃ ┣ 📂rfdc
 ┃ ┃ ┃ ┣ 📂.github
 ┃ ┃ ┃ ┃ ┗ 📂workflows
 ┃ ┃ ┃ ┃ ┃ ┗ 📜ci.yml
 ┃ ┃ ┃ ┣ 📂test
 ┃ ┃ ┃ ┃ ┗ 📜index.js
 ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┣ 📜default.js
 ┃ ┃ ┃ ┣ 📜index.d.ts
 ┃ ┃ ┃ ┣ 📜index.js
 ┃ ┃ ┃ ┣ 📜index.test-d.ts
 ┃ ┃ ┃ ┣ 📜package.json
 ┃ ┃ ┃ ┗ 📜readme.md
 ┃ ┃ ┣ 📂roarr
 ┃ ┃ ┃ ┣ 📂dist
 ┃ ┃ ┃ ┃ ┣ 📂factories
 ┃ ┃ ┃ ┃ ┃ ┣ 📜createLogger.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📜createLogger.js.flow
 ┃ ┃ ┃ ┃ ┃ ┣ 📜createLogger.js.map
 ┃ ┃ ┃ ┃ ┃ ┣ 📜createMockLogger.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📜createMockLogger.js.flow
 ┃ ┃ ┃ ┃ ┃ ┣ 📜createMockLogger.js.map
 ┃ ┃ ┃ ┃ ┃ ┣ 📜createNodeWriter.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📜createNodeWriter.js.flow
 ┃ ┃ ┃ ┃ ┃ ┣ 📜createNodeWriter.js.map
 ┃ ┃ ┃ ┃ ┃ ┣ 📜createRoarrInititialGlobalState.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📜createRoarrInititialGlobalState.js.flow
 ┃ ┃ ┃ ┃ ┃ ┣ 📜createRoarrInititialGlobalState.js.map
 ┃ ┃ ┃ ┃ ┃ ┣ 📜index.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📜index.js.flow
 ┃ ┃ ┃ ┃ ┃ ┗ 📜index.js.map
 ┃ ┃ ┃ ┃ ┣ 📜constants.js
 ┃ ┃ ┃ ┃ ┣ 📜constants.js.flow
 ┃ ┃ ┃ ┃ ┣ 📜constants.js.map
 ┃ ┃ ┃ ┃ ┣ 📜log.js
 ┃ ┃ ┃ ┃ ┣ 📜log.js.flow
 ┃ ┃ ┃ ┃ ┣ 📜log.js.map
 ┃ ┃ ┃ ┃ ┣ 📜types.js
 ┃ ┃ ┃ ┃ ┣ 📜types.js.flow
 ┃ ┃ ┃ ┃ ┗ 📜types.js.map
 ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┗ 📜package.json
 ┃ ┃ ┣ 📂rollup
 ┃ ┃ ┃ ┣ 📂dist
 ┃ ┃ ┃ ┃ ┣ 📂bin
 ┃ ┃ ┃ ┃ ┃ ┗ 📜rollup
 ┃ ┃ ┃ ┃ ┣ 📂es
 ┃ ┃ ┃ ┃ ┃ ┣ 📂shared
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜node-entry.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜parseAst.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜watch.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📜getLogFilter.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📜package.json
 ┃ ┃ ┃ ┃ ┃ ┣ 📜parseAst.js
 ┃ ┃ ┃ ┃ ┃ ┗ 📜rollup.js
 ┃ ┃ ┃ ┃ ┣ 📂shared
 ┃ ┃ ┃ ┃ ┃ ┣ 📜fsevents-importer.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📜index.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📜loadConfigFile.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📜parseAst.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📜rollup.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📜watch-cli.js
 ┃ ┃ ┃ ┃ ┃ ┗ 📜watch.js
 ┃ ┃ ┃ ┃ ┣ 📜getLogFilter.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜getLogFilter.js
 ┃ ┃ ┃ ┃ ┣ 📜loadConfigFile.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜loadConfigFile.js
 ┃ ┃ ┃ ┃ ┣ 📜native.js
 ┃ ┃ ┃ ┃ ┣ 📜parseAst.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜parseAst.js
 ┃ ┃ ┃ ┃ ┣ 📜rollup.d.ts
 ┃ ┃ ┃ ┃ ┗ 📜rollup.js
 ┃ ┃ ┃ ┣ 📜LICENSE.md
 ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┗ 📜package.json
 ┃ ┃ ┣ 📂scule
 ┃ ┃ ┃ ┣ 📂dist
 ┃ ┃ ┃ ┃ ┣ 📜index.cjs
 ┃ ┃ ┃ ┃ ┣ 📜index.d.cts
 ┃ ┃ ┃ ┃ ┣ 📜index.d.mts
 ┃ ┃ ┃ ┃ ┣ 📜index.d.ts
 ┃ ┃ ┃ ┃ ┗ 📜index.mjs
 ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┗ 📜package.json
 ┃ ┃ ┣ 📂semver
 ┃ ┃ ┃ ┣ 📂bin
 ┃ ┃ ┃ ┃ ┗ 📜semver.js
 ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┣ 📜package.json
 ┃ ┃ ┃ ┣ 📜range.bnf
 ┃ ┃ ┃ ┗ 📜semver.js
 ┃ ┃ ┣ 📂semver-compare
 ┃ ┃ ┃ ┣ 📂example
 ┃ ┃ ┃ ┃ ┣ 📜cmp.js
 ┃ ┃ ┃ ┃ ┗ 📜lex.js
 ┃ ┃ ┃ ┣ 📂test
 ┃ ┃ ┃ ┃ ┗ 📜cmp.js
 ┃ ┃ ┃ ┣ 📜.travis.yml
 ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┣ 📜index.js
 ┃ ┃ ┃ ┣ 📜package.json
 ┃ ┃ ┃ ┗ 📜readme.markdown
 ┃ ┃ ┣ 📂serialize-error
 ┃ ┃ ┃ ┣ 📜index.d.ts
 ┃ ┃ ┃ ┣ 📜index.js
 ┃ ┃ ┃ ┣ 📜license
 ┃ ┃ ┃ ┣ 📜package.json
 ┃ ┃ ┃ ┗ 📜readme.md
 ┃ ┃ ┣ 📂source-map-js
 ┃ ┃ ┃ ┣ 📂lib
 ┃ ┃ ┃ ┃ ┣ 📜array-set.js
 ┃ ┃ ┃ ┃ ┣ 📜base64-vlq.js
 ┃ ┃ ┃ ┃ ┣ 📜base64.js
 ┃ ┃ ┃ ┃ ┣ 📜binary-search.js
 ┃ ┃ ┃ ┃ ┣ 📜mapping-list.js
 ┃ ┃ ┃ ┃ ┣ 📜quick-sort.js
 ┃ ┃ ┃ ┃ ┣ 📜source-map-consumer.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜source-map-consumer.js
 ┃ ┃ ┃ ┃ ┣ 📜source-map-generator.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜source-map-generator.js
 ┃ ┃ ┃ ┃ ┣ 📜source-node.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜source-node.js
 ┃ ┃ ┃ ┃ ┗ 📜util.js
 ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┣ 📜package.json
 ┃ ┃ ┃ ┣ 📜source-map.d.ts
 ┃ ┃ ┃ ┗ 📜source-map.js
 ┃ ┃ ┣ 📂speakingurl
 ┃ ┃ ┃ ┣ 📂examples
 ┃ ┃ ┃ ┃ ┣ 📜browser-example.html
 ┃ ┃ ┃ ┃ ┗ 📜node-example.js
 ┃ ┃ ┃ ┣ 📂lib
 ┃ ┃ ┃ ┃ ┣ 📜speakingurl-rails.rb
 ┃ ┃ ┃ ┃ ┗ 📜speakingurl.js
 ┃ ┃ ┃ ┣ 📂test
 ┃ ┃ ┃ ┃ ┣ 📜mocha.opts
 ┃ ┃ ┃ ┃ ┣ 📜test-accent.js
 ┃ ┃ ┃ ┃ ┣ 📜test-arabic.js
 ┃ ┃ ┃ ┃ ┣ 📜test-burmese.js
 ┃ ┃ ┃ ┃ ┣ 📜test-create.js
 ┃ ┃ ┃ ┃ ┣ 📜test-custom.js
 ┃ ┃ ┃ ┃ ┣ 📜test-cyrillic.js
 ┃ ┃ ┃ ┃ ┣ 📜test-defaults.js
 ┃ ┃ ┃ ┃ ┣ 📜test-dhivehi.js
 ┃ ┃ ┃ ┃ ┣ 📜test-georgien.js
 ┃ ┃ ┃ ┃ ┣ 📜test-hungarian.js
 ┃ ┃ ┃ ┃ ┣ 📜test-lang.js
 ┃ ┃ ┃ ┃ ┣ 📜test-language.js
 ┃ ┃ ┃ ┃ ┣ 📜test-maintaincase.js
 ┃ ┃ ┃ ┃ ┣ 📜test-persian.js
 ┃ ┃ ┃ ┃ ┣ 📜test-rfc3986.js
 ┃ ┃ ┃ ┃ ┣ 📜test-separator.js
 ┃ ┃ ┃ ┃ ┣ 📜test-speakingurl.js
 ┃ ┃ ┃ ┃ ┣ 📜test-symbols.js
 ┃ ┃ ┃ ┃ ┣ 📜test-titlecase.js
 ┃ ┃ ┃ ┃ ┣ 📜test-truncate.js
 ┃ ┃ ┃ ┃ ┗ 📜test-turkish.js
 ┃ ┃ ┃ ┣ 📂typings
 ┃ ┃ ┃ ┃ ┗ 📂speakingurl
 ┃ ┃ ┃ ┃ ┃ ┗ 📜speakingurl.d.ts
 ┃ ┃ ┃ ┣ 📜.editorconfig
 ┃ ┃ ┃ ┣ 📜.jsbeautifyrc
 ┃ ┃ ┃ ┣ 📜.jshintignore
 ┃ ┃ ┃ ┣ 📜.jshintrc
 ┃ ┃ ┃ ┣ 📜.npmignore
 ┃ ┃ ┃ ┣ 📜.travis.yml
 ┃ ┃ ┃ ┣ 📜CHANGELOG.md
 ┃ ┃ ┃ ┣ 📜Gulpfile.js
 ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┣ 📜Makefile
 ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┣ 📜bower.json
 ┃ ┃ ┃ ┣ 📜component.json
 ┃ ┃ ┃ ┣ 📜index.js
 ┃ ┃ ┃ ┣ 📜package.json
 ┃ ┃ ┃ ┣ 📜speakingurl-rails.gemspec
 ┃ ┃ ┃ ┗ 📜speakingurl.min.js
 ┃ ┃ ┣ 📂sprintf-js
 ┃ ┃ ┃ ┣ 📂dist
 ┃ ┃ ┃ ┃ ┣ 📜.gitattributes
 ┃ ┃ ┃ ┃ ┣ 📜angular-sprintf.min.js
 ┃ ┃ ┃ ┃ ┣ 📜angular-sprintf.min.js.map
 ┃ ┃ ┃ ┃ ┣ 📜sprintf.min.js
 ┃ ┃ ┃ ┃ ┗ 📜sprintf.min.js.map
 ┃ ┃ ┃ ┣ 📂src
 ┃ ┃ ┃ ┃ ┣ 📜angular-sprintf.js
 ┃ ┃ ┃ ┃ ┗ 📜sprintf.js
 ┃ ┃ ┃ ┣ 📜CONTRIBUTORS.md
 ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┗ 📜package.json
 ┃ ┃ ┣ 📂sumchecker
 ┃ ┃ ┃ ┣ 📂.github
 ┃ ┃ ┃ ┃ ┣ 📂workflows
 ┃ ┃ ┃ ┃ ┃ ┗ 📜ci.yml
 ┃ ┃ ┃ ┃ ┗ 📜FUNDING.yml
 ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┣ 📜NEWS.md
 ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┣ 📜index.d.ts
 ┃ ┃ ┃ ┣ 📜index.js
 ┃ ┃ ┃ ┣ 📜index.test-d.ts
 ┃ ┃ ┃ ┣ 📜package.json
 ┃ ┃ ┃ ┗ 📜yarn.lock
 ┃ ┃ ┣ 📂superjson
 ┃ ┃ ┃ ┣ 📂dist
 ┃ ┃ ┃ ┃ ┣ 📜accessDeep.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜accessDeep.js
 ┃ ┃ ┃ ┃ ┣ 📜accessDeep.js.map
 ┃ ┃ ┃ ┃ ┣ 📜class-registry.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜class-registry.js
 ┃ ┃ ┃ ┃ ┣ 📜class-registry.js.map
 ┃ ┃ ┃ ┃ ┣ 📜custom-transformer-registry.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜custom-transformer-registry.js
 ┃ ┃ ┃ ┃ ┣ 📜custom-transformer-registry.js.map
 ┃ ┃ ┃ ┃ ┣ 📜double-indexed-kv.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜double-indexed-kv.js
 ┃ ┃ ┃ ┃ ┣ 📜double-indexed-kv.js.map
 ┃ ┃ ┃ ┃ ┣ 📜index.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜index.js
 ┃ ┃ ┃ ┃ ┣ 📜index.js.map
 ┃ ┃ ┃ ┃ ┣ 📜is.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜is.js
 ┃ ┃ ┃ ┃ ┣ 📜is.js.map
 ┃ ┃ ┃ ┃ ┣ 📜pathstringifier.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜pathstringifier.js
 ┃ ┃ ┃ ┃ ┣ 📜pathstringifier.js.map
 ┃ ┃ ┃ ┃ ┣ 📜plainer.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜plainer.js
 ┃ ┃ ┃ ┃ ┣ 📜plainer.js.map
 ┃ ┃ ┃ ┃ ┣ 📜registry.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜registry.js
 ┃ ┃ ┃ ┃ ┣ 📜registry.js.map
 ┃ ┃ ┃ ┃ ┣ 📜transformer.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜transformer.js
 ┃ ┃ ┃ ┃ ┣ 📜transformer.js.map
 ┃ ┃ ┃ ┃ ┣ 📜types.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜types.js
 ┃ ┃ ┃ ┃ ┣ 📜types.js.map
 ┃ ┃ ┃ ┃ ┣ 📜util.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜util.js
 ┃ ┃ ┃ ┃ ┗ 📜util.js.map
 ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┗ 📜package.json
 ┃ ┃ ┣ 📂tinyglobby
 ┃ ┃ ┃ ┣ 📂dist
 ┃ ┃ ┃ ┃ ┣ 📜index.cjs
 ┃ ┃ ┃ ┃ ┣ 📜index.d.cts
 ┃ ┃ ┃ ┃ ┣ 📜index.d.mts
 ┃ ┃ ┃ ┃ ┗ 📜index.mjs
 ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┗ 📜package.json
 ┃ ┃ ┣ 📂type-fest
 ┃ ┃ ┃ ┣ 📂source
 ┃ ┃ ┃ ┃ ┣ 📜async-return-type.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜basic.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜conditional-except.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜conditional-keys.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜conditional-pick.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜except.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜literal-union.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜merge-exclusive.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜merge.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜mutable.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜opaque.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜package-json.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜partial-deep.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜promisable.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜promise-value.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜readonly-deep.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜require-at-least-one.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜require-exactly-one.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜set-optional.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜set-required.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜stringified.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜tsconfig-json.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜union-to-intersection.d.ts
 ┃ ┃ ┃ ┃ ┗ 📜value-of.d.ts
 ┃ ┃ ┃ ┣ 📜index.d.ts
 ┃ ┃ ┃ ┣ 📜license
 ┃ ┃ ┃ ┣ 📜package.json
 ┃ ┃ ┃ ┗ 📜readme.md
 ┃ ┃ ┣ 📂ufo
 ┃ ┃ ┃ ┣ 📂dist
 ┃ ┃ ┃ ┃ ┣ 📜index.cjs
 ┃ ┃ ┃ ┃ ┣ 📜index.d.cts
 ┃ ┃ ┃ ┃ ┣ 📜index.d.mts
 ┃ ┃ ┃ ┃ ┣ 📜index.d.ts
 ┃ ┃ ┃ ┃ ┗ 📜index.mjs
 ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┗ 📜package.json
 ┃ ┃ ┣ 📂undici-types
 ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┣ 📜agent.d.ts
 ┃ ┃ ┃ ┣ 📜api.d.ts
 ┃ ┃ ┃ ┣ 📜balanced-pool.d.ts
 ┃ ┃ ┃ ┣ 📜cache-interceptor.d.ts
 ┃ ┃ ┃ ┣ 📜cache.d.ts
 ┃ ┃ ┃ ┣ 📜client-stats.d.ts
 ┃ ┃ ┃ ┣ 📜client.d.ts
 ┃ ┃ ┃ ┣ 📜connector.d.ts
 ┃ ┃ ┃ ┣ 📜content-type.d.ts
 ┃ ┃ ┃ ┣ 📜cookies.d.ts
 ┃ ┃ ┃ ┣ 📜diagnostics-channel.d.ts
 ┃ ┃ ┃ ┣ 📜dispatcher.d.ts
 ┃ ┃ ┃ ┣ 📜env-http-proxy-agent.d.ts
 ┃ ┃ ┃ ┣ 📜errors.d.ts
 ┃ ┃ ┃ ┣ 📜eventsource.d.ts
 ┃ ┃ ┃ ┣ 📜fetch.d.ts
 ┃ ┃ ┃ ┣ 📜formdata.d.ts
 ┃ ┃ ┃ ┣ 📜global-dispatcher.d.ts
 ┃ ┃ ┃ ┣ 📜global-origin.d.ts
 ┃ ┃ ┃ ┣ 📜h2c-client.d.ts
 ┃ ┃ ┃ ┣ 📜handlers.d.ts
 ┃ ┃ ┃ ┣ 📜header.d.ts
 ┃ ┃ ┃ ┣ 📜index.d.ts
 ┃ ┃ ┃ ┣ 📜interceptors.d.ts
 ┃ ┃ ┃ ┣ 📜mock-agent.d.ts
 ┃ ┃ ┃ ┣ 📜mock-call-history.d.ts
 ┃ ┃ ┃ ┣ 📜mock-client.d.ts
 ┃ ┃ ┃ ┣ 📜mock-errors.d.ts
 ┃ ┃ ┃ ┣ 📜mock-interceptor.d.ts
 ┃ ┃ ┃ ┣ 📜mock-pool.d.ts
 ┃ ┃ ┃ ┣ 📜package.json
 ┃ ┃ ┃ ┣ 📜patch.d.ts
 ┃ ┃ ┃ ┣ 📜pool-stats.d.ts
 ┃ ┃ ┃ ┣ 📜pool.d.ts
 ┃ ┃ ┃ ┣ 📜proxy-agent.d.ts
 ┃ ┃ ┃ ┣ 📜readable.d.ts
 ┃ ┃ ┃ ┣ 📜retry-agent.d.ts
 ┃ ┃ ┃ ┣ 📜retry-handler.d.ts
 ┃ ┃ ┃ ┣ 📜snapshot-agent.d.ts
 ┃ ┃ ┃ ┣ 📜util.d.ts
 ┃ ┃ ┃ ┣ 📜utility.d.ts
 ┃ ┃ ┃ ┣ 📜webidl.d.ts
 ┃ ┃ ┃ ┗ 📜websocket.d.ts
 ┃ ┃ ┣ 📂universalify
 ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┣ 📜index.js
 ┃ ┃ ┃ ┗ 📜package.json
 ┃ ┃ ┣ 📂unplugin
 ┃ ┃ ┃ ┣ 📂dist
 ┃ ┃ ┃ ┃ ┣ 📂rspack
 ┃ ┃ ┃ ┃ ┃ ┗ 📂loaders
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜load.d.mts
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜load.mjs
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜transform.d.mts
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜transform.mjs
 ┃ ┃ ┃ ┃ ┣ 📂webpack
 ┃ ┃ ┃ ┃ ┃ ┗ 📂loaders
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜load.d.mts
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜load.mjs
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜transform.d.mts
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜transform.mjs
 ┃ ┃ ┃ ┃ ┣ 📜context-CKhLGGrj.mjs
 ┃ ┃ ┃ ┃ ┣ 📜context-MD-xQmYI.mjs
 ┃ ┃ ┃ ┃ ┣ 📜index.d.mts
 ┃ ┃ ┃ ┃ ┣ 📜index.mjs
 ┃ ┃ ┃ ┃ ┣ 📜parse-DN2jPtpt.mjs
 ┃ ┃ ┃ ┃ ┣ 📜utils-BMHLEWml.mjs
 ┃ ┃ ┃ ┃ ┗ 📜webpack-like-Djrmy9eu.mjs
 ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┗ 📜package.json
 ┃ ┃ ┣ 📂unplugin-utils
 ┃ ┃ ┃ ┣ 📂dist
 ┃ ┃ ┃ ┃ ┣ 📜index.d.ts
 ┃ ┃ ┃ ┃ ┗ 📜index.js
 ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┗ 📜package.json
 ┃ ┃ ┣ 📂vite
 ┃ ┃ ┃ ┣ 📂bin
 ┃ ┃ ┃ ┃ ┣ 📜openChrome.js
 ┃ ┃ ┃ ┃ ┗ 📜vite.js
 ┃ ┃ ┃ ┣ 📂dist
 ┃ ┃ ┃ ┃ ┣ 📂client
 ┃ ┃ ┃ ┃ ┃ ┣ 📜client.mjs
 ┃ ┃ ┃ ┃ ┃ ┗ 📜env.mjs
 ┃ ┃ ┃ ┃ ┗ 📂node
 ┃ ┃ ┃ ┃ ┃ ┣ 📂chunks
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜build.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜build2.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜chunk.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜config.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜config2.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜dist.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜lib.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜logger.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜moduleRunnerTransport.d.ts
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜optimizer.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜postcss-import.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜preview.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜server.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📜cli.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📜index.d.ts
 ┃ ┃ ┃ ┃ ┃ ┣ 📜index.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📜module-runner.d.ts
 ┃ ┃ ┃ ┃ ┃ ┗ 📜module-runner.js
 ┃ ┃ ┃ ┣ 📂misc
 ┃ ┃ ┃ ┃ ┣ 📜false.js
 ┃ ┃ ┃ ┃ ┗ 📜true.js
 ┃ ┃ ┃ ┣ 📂types
 ┃ ┃ ┃ ┃ ┣ 📂internal
 ┃ ┃ ┃ ┃ ┃ ┣ 📜cssPreprocessorOptions.d.ts
 ┃ ┃ ┃ ┃ ┃ ┣ 📜lightningcssOptions.d.ts
 ┃ ┃ ┃ ┃ ┃ ┗ 📜terserOptions.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜customEvent.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜hmrPayload.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜hot.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜import-meta.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜importGlob.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜importMeta.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜metadata.d.ts
 ┃ ┃ ┃ ┃ ┗ 📜package.json
 ┃ ┃ ┃ ┣ 📜LICENSE.md
 ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┣ 📜client.d.ts
 ┃ ┃ ┃ ┗ 📜package.json
 ┃ ┃ ┣ 📂vue
 ┃ ┃ ┃ ┣ 📂compiler-sfc
 ┃ ┃ ┃ ┃ ┣ 📜index.browser.js
 ┃ ┃ ┃ ┃ ┣ 📜index.browser.mjs
 ┃ ┃ ┃ ┃ ┣ 📜index.d.mts
 ┃ ┃ ┃ ┃ ┣ 📜index.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜index.js
 ┃ ┃ ┃ ┃ ┣ 📜index.mjs
 ┃ ┃ ┃ ┃ ┣ 📜package.json
 ┃ ┃ ┃ ┃ ┗ 📜register-ts.js
 ┃ ┃ ┃ ┣ 📂dist
 ┃ ┃ ┃ ┃ ┣ 📜vue.cjs.js
 ┃ ┃ ┃ ┃ ┣ 📜vue.cjs.prod.js
 ┃ ┃ ┃ ┃ ┣ 📜vue.d.mts
 ┃ ┃ ┃ ┃ ┣ 📜vue.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜vue.esm-browser.js
 ┃ ┃ ┃ ┃ ┣ 📜vue.esm-browser.prod.js
 ┃ ┃ ┃ ┃ ┣ 📜vue.esm-bundler.js
 ┃ ┃ ┃ ┃ ┣ 📜vue.global.js
 ┃ ┃ ┃ ┃ ┣ 📜vue.global.prod.js
 ┃ ┃ ┃ ┃ ┣ 📜vue.runtime.esm-browser.js
 ┃ ┃ ┃ ┃ ┣ 📜vue.runtime.esm-browser.prod.js
 ┃ ┃ ┃ ┃ ┣ 📜vue.runtime.esm-bundler.js
 ┃ ┃ ┃ ┃ ┣ 📜vue.runtime.global.js
 ┃ ┃ ┃ ┃ ┗ 📜vue.runtime.global.prod.js
 ┃ ┃ ┃ ┣ 📂jsx-runtime
 ┃ ┃ ┃ ┃ ┣ 📜index.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜index.js
 ┃ ┃ ┃ ┃ ┣ 📜index.mjs
 ┃ ┃ ┃ ┃ ┗ 📜package.json
 ┃ ┃ ┃ ┣ 📂server-renderer
 ┃ ┃ ┃ ┃ ┣ 📜index.d.mts
 ┃ ┃ ┃ ┃ ┣ 📜index.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜index.js
 ┃ ┃ ┃ ┃ ┣ 📜index.mjs
 ┃ ┃ ┃ ┃ ┗ 📜package.json
 ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┣ 📜index.js
 ┃ ┃ ┃ ┣ 📜index.mjs
 ┃ ┃ ┃ ┣ 📜jsx.d.ts
 ┃ ┃ ┃ ┗ 📜package.json
 ┃ ┃ ┣ 📂vue-router
 ┃ ┃ ┃ ┣ 📂dist
 ┃ ┃ ┃ ┃ ┣ 📂experimental
 ┃ ┃ ┃ ┃ ┃ ┣ 📜index.d.mts
 ┃ ┃ ┃ ┃ ┃ ┣ 📜index.mjs
 ┃ ┃ ┃ ┃ ┃ ┣ 📜pinia-colada.d.mts
 ┃ ┃ ┃ ┃ ┃ ┗ 📜pinia-colada.mjs
 ┃ ┃ ┃ ┃ ┣ 📂unplugin
 ┃ ┃ ┃ ┃ ┃ ┣ 📜esbuild.cjs
 ┃ ┃ ┃ ┃ ┃ ┣ 📜esbuild.d.cts
 ┃ ┃ ┃ ┃ ┃ ┣ 📜esbuild.d.mts
 ┃ ┃ ┃ ┃ ┃ ┣ 📜esbuild.mjs
 ┃ ┃ ┃ ┃ ┃ ┣ 📜index.cjs
 ┃ ┃ ┃ ┃ ┃ ┣ 📜index.d.cts
 ┃ ┃ ┃ ┃ ┃ ┣ 📜index.d.mts
 ┃ ┃ ┃ ┃ ┃ ┣ 📜index.mjs
 ┃ ┃ ┃ ┃ ┃ ┣ 📜options.cjs
 ┃ ┃ ┃ ┃ ┃ ┣ 📜options.d.cts
 ┃ ┃ ┃ ┃ ┃ ┣ 📜options.d.mts
 ┃ ┃ ┃ ┃ ┃ ┣ 📜options.mjs
 ┃ ┃ ┃ ┃ ┃ ┣ 📜rolldown.cjs
 ┃ ┃ ┃ ┃ ┃ ┣ 📜rolldown.d.cts
 ┃ ┃ ┃ ┃ ┃ ┣ 📜rolldown.d.mts
 ┃ ┃ ┃ ┃ ┃ ┣ 📜rolldown.mjs
 ┃ ┃ ┃ ┃ ┃ ┣ 📜rollup.cjs
 ┃ ┃ ┃ ┃ ┃ ┣ 📜rollup.d.cts
 ┃ ┃ ┃ ┃ ┃ ┣ 📜rollup.d.mts
 ┃ ┃ ┃ ┃ ┃ ┣ 📜rollup.mjs
 ┃ ┃ ┃ ┃ ┃ ┣ 📜types.cjs
 ┃ ┃ ┃ ┃ ┃ ┣ 📜types.d.cts
 ┃ ┃ ┃ ┃ ┃ ┣ 📜types.d.mts
 ┃ ┃ ┃ ┃ ┃ ┣ 📜types.mjs
 ┃ ┃ ┃ ┃ ┃ ┣ 📜vite.cjs
 ┃ ┃ ┃ ┃ ┃ ┣ 📜vite.d.cts
 ┃ ┃ ┃ ┃ ┃ ┣ 📜vite.d.mts
 ┃ ┃ ┃ ┃ ┃ ┣ 📜vite.mjs
 ┃ ┃ ┃ ┃ ┃ ┣ 📜webpack.cjs
 ┃ ┃ ┃ ┃ ┃ ┣ 📜webpack.d.cts
 ┃ ┃ ┃ ┃ ┃ ┣ 📜webpack.d.mts
 ┃ ┃ ┃ ┃ ┃ ┗ 📜webpack.mjs
 ┃ ┃ ┃ ┃ ┣ 📂volar
 ┃ ┃ ┃ ┃ ┃ ┣ 📜sfc-route-blocks.cjs
 ┃ ┃ ┃ ┃ ┃ ┣ 📜sfc-route-blocks.d.cts
 ┃ ┃ ┃ ┃ ┃ ┣ 📜sfc-typed-router.cjs
 ┃ ┃ ┃ ┃ ┃ ┗ 📜sfc-typed-router.d.cts
 ┃ ┃ ┃ ┃ ┣ 📜devtools-CQC1vVRY.mjs
 ┃ ┃ ┃ ┃ ┣ 📜index-CUL6Z3eo.d.mts
 ┃ ┃ ┃ ┃ ┣ 📜index-Cu9B0wDz.d.mts
 ┃ ┃ ┃ ┃ ┣ 📜navigation-guard-eDUoFL1h.mjs
 ┃ ┃ ┃ ┃ ┣ 📜options-CjwwR_07.d.cts
 ┃ ┃ ┃ ┃ ┣ 📜options-DOL2pVRG.mjs
 ┃ ┃ ┃ ┃ ┣ 📜options-UcrzengD.d.mts
 ┃ ┃ ┃ ┃ ┣ 📜options-yLu3dPlU.cjs
 ┃ ┃ ┃ ┃ ┣ 📜unplugin-B7JVCLUR.mjs
 ┃ ┃ ┃ ┃ ┣ 📜unplugin-DeVsHA1K.cjs
 ┃ ┃ ┃ ┃ ┣ 📜useApi-o-nPpLEi.mjs
 ┃ ┃ ┃ ┃ ┣ 📜vue-router.cjs
 ┃ ┃ ┃ ┃ ┣ 📜vue-router.d.mts
 ┃ ┃ ┃ ┃ ┣ 📜vue-router.esm-browser.js
 ┃ ┃ ┃ ┃ ┣ 📜vue-router.esm-browser.prod.js
 ┃ ┃ ┃ ┃ ┣ 📜vue-router.esm-bundler.js
 ┃ ┃ ┃ ┃ ┣ 📜vue-router.global.js
 ┃ ┃ ┃ ┃ ┣ 📜vue-router.global.prod.js
 ┃ ┃ ┃ ┃ ┣ 📜vue-router.mjs
 ┃ ┃ ┃ ┃ ┗ 📜vue-router.prod.cjs
 ┃ ┃ ┃ ┣ 📂node_modules
 ┃ ┃ ┃ ┃ ┣ 📂@vue
 ┃ ┃ ┃ ┃ ┃ ┣ 📂devtools-api
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂dist
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜chunk.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜index.cjs
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜index.d.cts
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜index.d.ts
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜index.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜vue-devtools-api.esm-browser.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜vue-devtools-api.global.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜package.json
 ┃ ┃ ┃ ┃ ┃ ┣ 📂devtools-kit
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂dist
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜index.cjs
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜index.d.cts
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜index.d.ts
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜index.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜global.d.ts
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜package.json
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜types.d.ts
 ┃ ┃ ┃ ┃ ┃ ┗ 📂devtools-shared
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂dist
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜index.cjs
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜index.d.cts
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜index.d.ts
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜index.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜package.json
 ┃ ┃ ┃ ┃ ┗ 📂perfect-debounce
 ┃ ┃ ┃ ┃ ┃ ┣ 📂dist
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜index.d.mts
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜index.mjs
 ┃ ┃ ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┃ ┃ ┗ 📜package.json
 ┃ ┃ ┃ ┣ 📂vetur
 ┃ ┃ ┃ ┃ ┣ 📜attributes.json
 ┃ ┃ ┃ ┃ ┗ 📜tags.json
 ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┣ 📜index.js
 ┃ ┃ ┃ ┣ 📜package.json
 ┃ ┃ ┃ ┣ 📜route.schema.json
 ┃ ┃ ┃ ┣ 📜vue-router-auto-resolver.d.mts
 ┃ ┃ ┃ ┣ 📜vue-router-auto-routes.d.mts
 ┃ ┃ ┃ ┣ 📜vue-router-auto.d.ts
 ┃ ┃ ┃ ┗ 📜vue-router.node.mjs
 ┃ ┃ ┣ 📂webpack-virtual-modules
 ┃ ┃ ┃ ┣ 📂lib
 ┃ ┃ ┃ ┃ ┣ 📜index.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜index.js
 ┃ ┃ ┃ ┃ ┣ 📜index.js.map
 ┃ ┃ ┃ ┃ ┣ 📜virtual-stats.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜virtual-stats.js
 ┃ ┃ ┃ ┃ ┗ 📜virtual-stats.js.map
 ┃ ┃ ┃ ┣ 📂src
 ┃ ┃ ┃ ┃ ┣ 📜index.ts
 ┃ ┃ ┃ ┃ ┗ 📜virtual-stats.ts
 ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┗ 📜package.json
 ┃ ┃ ┣ 📂wrappy
 ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┣ 📜package.json
 ┃ ┃ ┃ ┗ 📜wrappy.js
 ┃ ┃ ┣ 📂yaml
 ┃ ┃ ┃ ┣ 📂browser
 ┃ ┃ ┃ ┃ ┣ 📂dist
 ┃ ┃ ┃ ┃ ┃ ┣ 📂compose
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜compose-collection.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜compose-doc.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜compose-node.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜compose-scalar.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜composer.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜resolve-block-map.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜resolve-block-scalar.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜resolve-block-seq.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜resolve-end.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜resolve-flow-collection.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜resolve-flow-scalar.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜resolve-props.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜util-contains-newline.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜util-empty-scalar-position.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜util-flow-indent-check.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜util-map-includes.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📂doc
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Document.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜anchors.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜applyReviver.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜createNode.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜directives.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📂nodes
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Alias.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Collection.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Node.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Pair.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Scalar.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜YAMLMap.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜YAMLSeq.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜addPairToJSMap.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜identity.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜toJS.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📂parse
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cst-scalar.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cst-stringify.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cst-visit.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜cst.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜lexer.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜line-counter.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜parser.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📂schema
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂common
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜map.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜null.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜seq.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜string.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂core
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜bool.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜float.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜int.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜schema.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂json
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜schema.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂yaml-1.1
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜binary.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜bool.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜float.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜int.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜merge.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜omap.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pairs.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜schema.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜set.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜timestamp.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Schema.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜tags.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📂stringify
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜foldFlowLines.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜stringify.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜stringifyCollection.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜stringifyComment.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜stringifyDocument.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜stringifyNumber.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜stringifyPair.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜stringifyString.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📜errors.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📜index.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📜log.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📜public-api.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📜util.js
 ┃ ┃ ┃ ┃ ┃ ┗ 📜visit.js
 ┃ ┃ ┃ ┃ ┣ 📜index.js
 ┃ ┃ ┃ ┃ ┗ 📜package.json
 ┃ ┃ ┃ ┣ 📂dist
 ┃ ┃ ┃ ┃ ┣ 📂compose
 ┃ ┃ ┃ ┃ ┃ ┣ 📜compose-collection.d.ts
 ┃ ┃ ┃ ┃ ┃ ┣ 📜compose-collection.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📜compose-doc.d.ts
 ┃ ┃ ┃ ┃ ┃ ┣ 📜compose-doc.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📜compose-node.d.ts
 ┃ ┃ ┃ ┃ ┃ ┣ 📜compose-node.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📜compose-scalar.d.ts
 ┃ ┃ ┃ ┃ ┃ ┣ 📜compose-scalar.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📜composer.d.ts
 ┃ ┃ ┃ ┃ ┃ ┣ 📜composer.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📜resolve-block-map.d.ts
 ┃ ┃ ┃ ┃ ┃ ┣ 📜resolve-block-map.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📜resolve-block-scalar.d.ts
 ┃ ┃ ┃ ┃ ┃ ┣ 📜resolve-block-scalar.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📜resolve-block-seq.d.ts
 ┃ ┃ ┃ ┃ ┃ ┣ 📜resolve-block-seq.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📜resolve-end.d.ts
 ┃ ┃ ┃ ┃ ┃ ┣ 📜resolve-end.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📜resolve-flow-collection.d.ts
 ┃ ┃ ┃ ┃ ┃ ┣ 📜resolve-flow-collection.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📜resolve-flow-scalar.d.ts
 ┃ ┃ ┃ ┃ ┃ ┣ 📜resolve-flow-scalar.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📜resolve-props.d.ts
 ┃ ┃ ┃ ┃ ┃ ┣ 📜resolve-props.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📜util-contains-newline.d.ts
 ┃ ┃ ┃ ┃ ┃ ┣ 📜util-contains-newline.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📜util-empty-scalar-position.d.ts
 ┃ ┃ ┃ ┃ ┃ ┣ 📜util-empty-scalar-position.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📜util-flow-indent-check.d.ts
 ┃ ┃ ┃ ┃ ┃ ┣ 📜util-flow-indent-check.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📜util-map-includes.d.ts
 ┃ ┃ ┃ ┃ ┃ ┗ 📜util-map-includes.js
 ┃ ┃ ┃ ┃ ┣ 📂doc
 ┃ ┃ ┃ ┃ ┃ ┣ 📜Document.d.ts
 ┃ ┃ ┃ ┃ ┃ ┣ 📜Document.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📜anchors.d.ts
 ┃ ┃ ┃ ┃ ┃ ┣ 📜anchors.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📜applyReviver.d.ts
 ┃ ┃ ┃ ┃ ┃ ┣ 📜applyReviver.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📜createNode.d.ts
 ┃ ┃ ┃ ┃ ┃ ┣ 📜createNode.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📜directives.d.ts
 ┃ ┃ ┃ ┃ ┃ ┗ 📜directives.js
 ┃ ┃ ┃ ┃ ┣ 📂nodes
 ┃ ┃ ┃ ┃ ┃ ┣ 📜Alias.d.ts
 ┃ ┃ ┃ ┃ ┃ ┣ 📜Alias.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📜Collection.d.ts
 ┃ ┃ ┃ ┃ ┃ ┣ 📜Collection.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📜Node.d.ts
 ┃ ┃ ┃ ┃ ┃ ┣ 📜Node.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📜Pair.d.ts
 ┃ ┃ ┃ ┃ ┃ ┣ 📜Pair.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📜Scalar.d.ts
 ┃ ┃ ┃ ┃ ┃ ┣ 📜Scalar.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📜YAMLMap.d.ts
 ┃ ┃ ┃ ┃ ┃ ┣ 📜YAMLMap.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📜YAMLSeq.d.ts
 ┃ ┃ ┃ ┃ ┃ ┣ 📜YAMLSeq.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📜addPairToJSMap.d.ts
 ┃ ┃ ┃ ┃ ┃ ┣ 📜addPairToJSMap.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📜identity.d.ts
 ┃ ┃ ┃ ┃ ┃ ┣ 📜identity.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📜toJS.d.ts
 ┃ ┃ ┃ ┃ ┃ ┗ 📜toJS.js
 ┃ ┃ ┃ ┃ ┣ 📂parse
 ┃ ┃ ┃ ┃ ┃ ┣ 📜cst-scalar.d.ts
 ┃ ┃ ┃ ┃ ┃ ┣ 📜cst-scalar.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📜cst-stringify.d.ts
 ┃ ┃ ┃ ┃ ┃ ┣ 📜cst-stringify.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📜cst-visit.d.ts
 ┃ ┃ ┃ ┃ ┃ ┣ 📜cst-visit.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📜cst.d.ts
 ┃ ┃ ┃ ┃ ┃ ┣ 📜cst.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📜lexer.d.ts
 ┃ ┃ ┃ ┃ ┃ ┣ 📜lexer.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📜line-counter.d.ts
 ┃ ┃ ┃ ┃ ┃ ┣ 📜line-counter.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📜parser.d.ts
 ┃ ┃ ┃ ┃ ┃ ┗ 📜parser.js
 ┃ ┃ ┃ ┃ ┣ 📂schema
 ┃ ┃ ┃ ┃ ┃ ┣ 📂common
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜map.d.ts
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜map.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜null.d.ts
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜null.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜seq.d.ts
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜seq.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜string.d.ts
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜string.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📂core
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜bool.d.ts
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜bool.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜float.d.ts
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜float.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜int.d.ts
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜int.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜schema.d.ts
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜schema.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📂json
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜schema.d.ts
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜schema.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📂yaml-1.1
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜binary.d.ts
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜binary.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜bool.d.ts
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜bool.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜float.d.ts
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜float.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜int.d.ts
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜int.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜merge.d.ts
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜merge.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜omap.d.ts
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜omap.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pairs.d.ts
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜pairs.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜schema.d.ts
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜schema.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜set.d.ts
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜set.js
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜timestamp.d.ts
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜timestamp.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📜Schema.d.ts
 ┃ ┃ ┃ ┃ ┃ ┣ 📜Schema.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📜json-schema.d.ts
 ┃ ┃ ┃ ┃ ┃ ┣ 📜tags.d.ts
 ┃ ┃ ┃ ┃ ┃ ┣ 📜tags.js
 ┃ ┃ ┃ ┃ ┃ ┗ 📜types.d.ts
 ┃ ┃ ┃ ┃ ┣ 📂stringify
 ┃ ┃ ┃ ┃ ┃ ┣ 📜foldFlowLines.d.ts
 ┃ ┃ ┃ ┃ ┃ ┣ 📜foldFlowLines.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📜stringify.d.ts
 ┃ ┃ ┃ ┃ ┃ ┣ 📜stringify.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📜stringifyCollection.d.ts
 ┃ ┃ ┃ ┃ ┃ ┣ 📜stringifyCollection.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📜stringifyComment.d.ts
 ┃ ┃ ┃ ┃ ┃ ┣ 📜stringifyComment.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📜stringifyDocument.d.ts
 ┃ ┃ ┃ ┃ ┃ ┣ 📜stringifyDocument.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📜stringifyNumber.d.ts
 ┃ ┃ ┃ ┃ ┃ ┣ 📜stringifyNumber.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📜stringifyPair.d.ts
 ┃ ┃ ┃ ┃ ┃ ┣ 📜stringifyPair.js
 ┃ ┃ ┃ ┃ ┃ ┣ 📜stringifyString.d.ts
 ┃ ┃ ┃ ┃ ┃ ┗ 📜stringifyString.js
 ┃ ┃ ┃ ┃ ┣ 📜cli.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜cli.mjs
 ┃ ┃ ┃ ┃ ┣ 📜errors.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜errors.js
 ┃ ┃ ┃ ┃ ┣ 📜index.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜index.js
 ┃ ┃ ┃ ┃ ┣ 📜log.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜log.js
 ┃ ┃ ┃ ┃ ┣ 📜options.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜public-api.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜public-api.js
 ┃ ┃ ┃ ┃ ┣ 📜test-events.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜test-events.js
 ┃ ┃ ┃ ┃ ┣ 📜util.d.ts
 ┃ ┃ ┃ ┃ ┣ 📜util.js
 ┃ ┃ ┃ ┃ ┣ 📜visit.d.ts
 ┃ ┃ ┃ ┃ ┗ 📜visit.js
 ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┣ 📜bin.mjs
 ┃ ┃ ┃ ┣ 📜package.json
 ┃ ┃ ┃ ┗ 📜util.js
 ┃ ┃ ┣ 📂yauzl
 ┃ ┃ ┃ ┣ 📜LICENSE
 ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┣ 📜index.js
 ┃ ┃ ┃ ┗ 📜package.json
 ┃ ┃ ┗ 📜.package-lock.json
 ┃ ┣ 📂public
 ┃ ┃ ┗ 📜vite.svg
 ┃ ┣ 📂src
 ┃ ┃ ┣ 📂api
 ┃ ┃ ┃ ┗ 📜axios.js
 ┃ ┃ ┣ 📂assets
 ┃ ┃ ┃ ┗ 📜vue.svg
 ┃ ┃ ┣ 📂components
 ┃ ┃ ┃ ┣ 📜EquipoPokemon.vue
 ┃ ┃ ┃ ┣ 📜ListaTareas.vue
 ┃ ┃ ┃ ┗ 📜PomodoroTimer.vue
 ┃ ┃ ┣ 📂utils
 ┃ ┃ ┃ ┗ 📜prettyAlert.js
 ┃ ┃ ┣ 📂views
 ┃ ┃ ┃ ┣ 📜DashboardView.vue
 ┃ ┃ ┃ ┣ 📜LoginView.vue
 ┃ ┃ ┃ ┣ 📜PCView.vue
 ┃ ┃ ┃ ┣ 📜PokedexView.vue
 ┃ ┃ ┃ ┣ 📜ProfileView.vue
 ┃ ┃ ┃ ┗ 📜RegistroView.vue
 ┃ ┃ ┣ 📜App.vue
 ┃ ┃ ┣ 📜main.js
 ┃ ┃ ┣ 📜router.js
 ┃ ┃ ┗ 📜style.css
 ┃ ┣ 📜.gitignore
 ┃ ┣ 📜README.md
 ┃ ┣ 📜index.html
 ┃ ┣ 📜package-lock.json
 ┃ ┣ 📜package.json
 ┃ ┗ 📜vite.config.js
 ┣ 📂media
 ┃ ┗ 📂pokemon
 ┃ ┃ ┣ 📂normal
 ┃ ┃ ┃ ┣ 📜abra.png
 ┃ ┃ ┃ ┣ 📜aerodactyl.png
 ┃ ┃ ┃ ┣ 📜alakazam.png
 ┃ ┃ ┃ ┣ 📜arbok.png
 ┃ ┃ ┃ ┣ 📜arcanine.png
 ┃ ┃ ┃ ┣ 📜articuno.png
 ┃ ┃ ┃ ┣ 📜beedrill.png
 ┃ ┃ ┃ ┣ 📜bellsprout.png
 ┃ ┃ ┃ ┣ 📜blastoise.png
 ┃ ┃ ┃ ┣ 📜bulbasaur.png
 ┃ ┃ ┃ ┣ 📜butterfree.png
 ┃ ┃ ┃ ┣ 📜caterpie.png
 ┃ ┃ ┃ ┣ 📜chansey.png
 ┃ ┃ ┃ ┣ 📜charizard.png
 ┃ ┃ ┃ ┣ 📜charmander.png
 ┃ ┃ ┃ ┣ 📜charmeleon.png
 ┃ ┃ ┃ ┣ 📜clefable.png
 ┃ ┃ ┃ ┣ 📜clefairy.png
 ┃ ┃ ┃ ┣ 📜cloyster.png
 ┃ ┃ ┃ ┣ 📜cubone.png
 ┃ ┃ ┃ ┣ 📜dewgong.png
 ┃ ┃ ┃ ┣ 📜diglett.png
 ┃ ┃ ┃ ┣ 📜ditto.png
 ┃ ┃ ┃ ┣ 📜dodrio.png
 ┃ ┃ ┃ ┣ 📜doduo.png
 ┃ ┃ ┃ ┣ 📜dragonair.png
 ┃ ┃ ┃ ┣ 📜dragonite.png
 ┃ ┃ ┃ ┣ 📜dratini.png
 ┃ ┃ ┃ ┣ 📜drowzee.png
 ┃ ┃ ┃ ┣ 📜dugtrio.png
 ┃ ┃ ┃ ┣ 📜eevee.png
 ┃ ┃ ┃ ┣ 📜ekans.png
 ┃ ┃ ┃ ┣ 📜electabuzz.png
 ┃ ┃ ┃ ┣ 📜electrode.png
 ┃ ┃ ┃ ┣ 📜exeggcute.png
 ┃ ┃ ┃ ┣ 📜exeggutor.png
 ┃ ┃ ┃ ┣ 📜farfetchd.png
 ┃ ┃ ┃ ┣ 📜fearow.png
 ┃ ┃ ┃ ┣ 📜flareon.png
 ┃ ┃ ┃ ┣ 📜gastly.png
 ┃ ┃ ┃ ┣ 📜gengar.png
 ┃ ┃ ┃ ┣ 📜geodude.png
 ┃ ┃ ┃ ┣ 📜gloom.png
 ┃ ┃ ┃ ┣ 📜golbat.png
 ┃ ┃ ┃ ┣ 📜goldeen.png
 ┃ ┃ ┃ ┣ 📜golduck.png
 ┃ ┃ ┃ ┣ 📜golem.png
 ┃ ┃ ┃ ┣ 📜graveler.png
 ┃ ┃ ┃ ┣ 📜grimer.png
 ┃ ┃ ┃ ┣ 📜growlithe.png
 ┃ ┃ ┃ ┣ 📜gyarados.png
 ┃ ┃ ┃ ┣ 📜haunter.png
 ┃ ┃ ┃ ┣ 📜hitmonchan.png
 ┃ ┃ ┃ ┣ 📜hitmonlee.png
 ┃ ┃ ┃ ┣ 📜horsea.png
 ┃ ┃ ┃ ┣ 📜hypno.png
 ┃ ┃ ┃ ┣ 📜ivysaur.png
 ┃ ┃ ┃ ┣ 📜jigglypuff.png
 ┃ ┃ ┃ ┣ 📜jolteon.png
 ┃ ┃ ┃ ┣ 📜jynx.png
 ┃ ┃ ┃ ┣ 📜kabuto.png
 ┃ ┃ ┃ ┣ 📜kabutops.png
 ┃ ┃ ┃ ┣ 📜kadabra.png
 ┃ ┃ ┃ ┣ 📜kakuna.png
 ┃ ┃ ┃ ┣ 📜kangaskhan.png
 ┃ ┃ ┃ ┣ 📜kingler.png
 ┃ ┃ ┃ ┣ 📜koffing.png
 ┃ ┃ ┃ ┣ 📜krabby.png
 ┃ ┃ ┃ ┣ 📜lapras.png
 ┃ ┃ ┃ ┣ 📜lickitung.png
 ┃ ┃ ┃ ┣ 📜machamp.png
 ┃ ┃ ┃ ┣ 📜machoke.png
 ┃ ┃ ┃ ┣ 📜machop.png
 ┃ ┃ ┃ ┣ 📜magikarp.png
 ┃ ┃ ┃ ┣ 📜magmar.png
 ┃ ┃ ┃ ┣ 📜magnemite.png
 ┃ ┃ ┃ ┣ 📜magneton.png
 ┃ ┃ ┃ ┣ 📜mankey.png
 ┃ ┃ ┃ ┣ 📜marowak.png
 ┃ ┃ ┃ ┣ 📜meowth.png
 ┃ ┃ ┃ ┣ 📜metapod.png
 ┃ ┃ ┃ ┣ 📜mew.png
 ┃ ┃ ┃ ┣ 📜mewtwo.png
 ┃ ┃ ┃ ┣ 📜moltres.png
 ┃ ┃ ┃ ┣ 📜mr-mime.png
 ┃ ┃ ┃ ┣ 📜muk.png
 ┃ ┃ ┃ ┣ 📜nidoking.png
 ┃ ┃ ┃ ┣ 📜nidoqueen.png
 ┃ ┃ ┃ ┣ 📜nidoran-f.png
 ┃ ┃ ┃ ┣ 📜nidoran-m.png
 ┃ ┃ ┃ ┣ 📜nidorina.png
 ┃ ┃ ┃ ┣ 📜nidorino.png
 ┃ ┃ ┃ ┣ 📜ninetales.png
 ┃ ┃ ┃ ┣ 📜oddish.png
 ┃ ┃ ┃ ┣ 📜omanyte.png
 ┃ ┃ ┃ ┣ 📜omastar.png
 ┃ ┃ ┃ ┣ 📜onix.png
 ┃ ┃ ┃ ┣ 📜paras.png
 ┃ ┃ ┃ ┣ 📜parasect.png
 ┃ ┃ ┃ ┣ 📜persian.png
 ┃ ┃ ┃ ┣ 📜pidgeot.png
 ┃ ┃ ┃ ┣ 📜pidgeotto.png
 ┃ ┃ ┃ ┣ 📜pidgey.png
 ┃ ┃ ┃ ┣ 📜pikachu.png
 ┃ ┃ ┃ ┣ 📜pinsir.png
 ┃ ┃ ┃ ┣ 📜poliwag.png
 ┃ ┃ ┃ ┣ 📜poliwhirl.png
 ┃ ┃ ┃ ┣ 📜poliwrath.png
 ┃ ┃ ┃ ┣ 📜ponyta.png
 ┃ ┃ ┃ ┣ 📜porygon.png
 ┃ ┃ ┃ ┣ 📜primeape.png
 ┃ ┃ ┃ ┣ 📜psyduck.png
 ┃ ┃ ┃ ┣ 📜raichu.png
 ┃ ┃ ┃ ┣ 📜rapidash.png
 ┃ ┃ ┃ ┣ 📜raticate.png
 ┃ ┃ ┃ ┣ 📜rattata.png
 ┃ ┃ ┃ ┣ 📜rhydon.png
 ┃ ┃ ┃ ┣ 📜rhyhorn.png
 ┃ ┃ ┃ ┣ 📜sandshrew.png
 ┃ ┃ ┃ ┣ 📜sandslash.png
 ┃ ┃ ┃ ┣ 📜scyther.png
 ┃ ┃ ┃ ┣ 📜seadra.png
 ┃ ┃ ┃ ┣ 📜seaking.png
 ┃ ┃ ┃ ┣ 📜seel.png
 ┃ ┃ ┃ ┣ 📜shellder.png
 ┃ ┃ ┃ ┣ 📜slowbro.png
 ┃ ┃ ┃ ┣ 📜slowpoke.png
 ┃ ┃ ┃ ┣ 📜snorlax.png
 ┃ ┃ ┃ ┣ 📜spearow.png
 ┃ ┃ ┃ ┣ 📜squirtle.png
 ┃ ┃ ┃ ┣ 📜starmie.png
 ┃ ┃ ┃ ┣ 📜staryu.png
 ┃ ┃ ┃ ┣ 📜tangela.png
 ┃ ┃ ┃ ┣ 📜tauros.png
 ┃ ┃ ┃ ┣ 📜tentacool.png
 ┃ ┃ ┃ ┣ 📜tentacruel.png
 ┃ ┃ ┃ ┣ 📜vaporeon.png
 ┃ ┃ ┃ ┣ 📜venomoth.png
 ┃ ┃ ┃ ┣ 📜venonat.png
 ┃ ┃ ┃ ┣ 📜venusaur.png
 ┃ ┃ ┃ ┣ 📜victreebel.png
 ┃ ┃ ┃ ┣ 📜vileplume.png
 ┃ ┃ ┃ ┣ 📜voltorb.png
 ┃ ┃ ┃ ┣ 📜vulpix.png
 ┃ ┃ ┃ ┣ 📜wartortle.png
 ┃ ┃ ┃ ┣ 📜weedle.png
 ┃ ┃ ┃ ┣ 📜weepinbell.png
 ┃ ┃ ┃ ┣ 📜weezing.png
 ┃ ┃ ┃ ┣ 📜wigglytuff.png
 ┃ ┃ ┃ ┣ 📜zapdos.png
 ┃ ┃ ┃ ┗ 📜zubat.png
 ┃ ┃ ┣ 📂shiny
 ┃ ┃ ┃ ┣ 📜abra.png
 ┃ ┃ ┃ ┣ 📜aerodactyl.png
 ┃ ┃ ┃ ┣ 📜alakazam.png
 ┃ ┃ ┃ ┣ 📜arbok.png
 ┃ ┃ ┃ ┣ 📜arcanine.png
 ┃ ┃ ┃ ┣ 📜articuno.png
 ┃ ┃ ┃ ┣ 📜beedrill.png
 ┃ ┃ ┃ ┣ 📜bellsprout.png
 ┃ ┃ ┃ ┣ 📜blastoise.png
 ┃ ┃ ┃ ┣ 📜bulbasaur.png
 ┃ ┃ ┃ ┣ 📜butterfree.png
 ┃ ┃ ┃ ┣ 📜caterpie.png
 ┃ ┃ ┃ ┣ 📜chansey.png
 ┃ ┃ ┃ ┣ 📜charizard.png
 ┃ ┃ ┃ ┣ 📜charmander.png
 ┃ ┃ ┃ ┣ 📜charmeleon.png
 ┃ ┃ ┃ ┣ 📜clefable.png
 ┃ ┃ ┃ ┣ 📜clefairy.png
 ┃ ┃ ┃ ┣ 📜cloyster.png
 ┃ ┃ ┃ ┣ 📜cubone.png
 ┃ ┃ ┃ ┣ 📜dewgong.png
 ┃ ┃ ┃ ┣ 📜diglett.png
 ┃ ┃ ┃ ┣ 📜ditto.png
 ┃ ┃ ┃ ┣ 📜dodrio.png
 ┃ ┃ ┃ ┣ 📜doduo.png
 ┃ ┃ ┃ ┣ 📜dragonair.png
 ┃ ┃ ┃ ┣ 📜dragonite.png
 ┃ ┃ ┃ ┣ 📜dratini.png
 ┃ ┃ ┃ ┣ 📜drowzee.png
 ┃ ┃ ┃ ┣ 📜dugtrio.png
 ┃ ┃ ┃ ┣ 📜eevee.png
 ┃ ┃ ┃ ┣ 📜ekans.png
 ┃ ┃ ┃ ┣ 📜electabuzz.png
 ┃ ┃ ┃ ┣ 📜electrode.png
 ┃ ┃ ┃ ┣ 📜exeggcute.png
 ┃ ┃ ┃ ┣ 📜exeggutor.png
 ┃ ┃ ┃ ┣ 📜farfetchd.png
 ┃ ┃ ┃ ┣ 📜fearow.png
 ┃ ┃ ┃ ┣ 📜flareon.png
 ┃ ┃ ┃ ┣ 📜gastly.png
 ┃ ┃ ┃ ┣ 📜gengar.png
 ┃ ┃ ┃ ┣ 📜geodude.png
 ┃ ┃ ┃ ┣ 📜gloom.png
 ┃ ┃ ┃ ┣ 📜golbat.png
 ┃ ┃ ┃ ┣ 📜goldeen.png
 ┃ ┃ ┃ ┣ 📜golduck.png
 ┃ ┃ ┃ ┣ 📜golem.png
 ┃ ┃ ┃ ┣ 📜graveler.png
 ┃ ┃ ┃ ┣ 📜grimer.png
 ┃ ┃ ┃ ┣ 📜growlithe.png
 ┃ ┃ ┃ ┣ 📜gyarados.png
 ┃ ┃ ┃ ┣ 📜haunter.png
 ┃ ┃ ┃ ┣ 📜hitmonchan.png
 ┃ ┃ ┃ ┣ 📜hitmonlee.png
 ┃ ┃ ┃ ┣ 📜horsea.png
 ┃ ┃ ┃ ┣ 📜hypno.png
 ┃ ┃ ┃ ┣ 📜ivysaur.png
 ┃ ┃ ┃ ┣ 📜jigglypuff.png
 ┃ ┃ ┃ ┣ 📜jolteon.png
 ┃ ┃ ┃ ┣ 📜jynx.png
 ┃ ┃ ┃ ┣ 📜kabuto.png
 ┃ ┃ ┃ ┣ 📜kabutops.png
 ┃ ┃ ┃ ┣ 📜kadabra.png
 ┃ ┃ ┃ ┣ 📜kakuna.png
 ┃ ┃ ┃ ┣ 📜kangaskhan.png
 ┃ ┃ ┃ ┣ 📜kingler.png
 ┃ ┃ ┃ ┣ 📜koffing.png
 ┃ ┃ ┃ ┣ 📜krabby.png
 ┃ ┃ ┃ ┣ 📜lapras.png
 ┃ ┃ ┃ ┣ 📜lickitung.png
 ┃ ┃ ┃ ┣ 📜machamp.png
 ┃ ┃ ┃ ┣ 📜machoke.png
 ┃ ┃ ┃ ┣ 📜machop.png
 ┃ ┃ ┃ ┣ 📜magikarp.png
 ┃ ┃ ┃ ┣ 📜magmar.png
 ┃ ┃ ┃ ┣ 📜magnemite.png
 ┃ ┃ ┃ ┣ 📜magneton.png
 ┃ ┃ ┃ ┣ 📜mankey.png
 ┃ ┃ ┃ ┣ 📜marowak.png
 ┃ ┃ ┃ ┣ 📜meowth.png
 ┃ ┃ ┃ ┣ 📜metapod.png
 ┃ ┃ ┃ ┣ 📜mew.png
 ┃ ┃ ┃ ┣ 📜mewtwo.png
 ┃ ┃ ┃ ┣ 📜moltres.png
 ┃ ┃ ┃ ┣ 📜mr-mime.png
 ┃ ┃ ┃ ┣ 📜muk.png
 ┃ ┃ ┃ ┣ 📜nidoking.png
 ┃ ┃ ┃ ┣ 📜nidoqueen.png
 ┃ ┃ ┃ ┣ 📜nidoran-f.png
 ┃ ┃ ┃ ┣ 📜nidoran-m.png
 ┃ ┃ ┃ ┣ 📜nidorina.png
 ┃ ┃ ┃ ┣ 📜nidorino.png
 ┃ ┃ ┃ ┣ 📜ninetales.png
 ┃ ┃ ┃ ┣ 📜oddish.png
 ┃ ┃ ┃ ┣ 📜omanyte.png
 ┃ ┃ ┃ ┣ 📜omastar.png
 ┃ ┃ ┃ ┣ 📜onix.png
 ┃ ┃ ┃ ┣ 📜paras.png
 ┃ ┃ ┃ ┣ 📜parasect.png
 ┃ ┃ ┃ ┣ 📜persian.png
 ┃ ┃ ┃ ┣ 📜pidgeot.png
 ┃ ┃ ┃ ┣ 📜pidgeotto.png
 ┃ ┃ ┃ ┣ 📜pidgey.png
 ┃ ┃ ┃ ┣ 📜pikachu.png
 ┃ ┃ ┃ ┣ 📜pinsir.png
 ┃ ┃ ┃ ┣ 📜poliwag.png
 ┃ ┃ ┃ ┣ 📜poliwhirl.png
 ┃ ┃ ┃ ┣ 📜poliwrath.png
 ┃ ┃ ┃ ┣ 📜ponyta.png
 ┃ ┃ ┃ ┣ 📜porygon.png
 ┃ ┃ ┃ ┣ 📜primeape.png
 ┃ ┃ ┃ ┣ 📜psyduck.png
 ┃ ┃ ┃ ┣ 📜raichu.png
 ┃ ┃ ┃ ┣ 📜rapidash.png
 ┃ ┃ ┃ ┣ 📜raticate.png
 ┃ ┃ ┃ ┣ 📜rattata.png
 ┃ ┃ ┃ ┣ 📜rhydon.png
 ┃ ┃ ┃ ┣ 📜rhyhorn.png
 ┃ ┃ ┃ ┣ 📜sandshrew.png
 ┃ ┃ ┃ ┣ 📜sandslash.png
 ┃ ┃ ┃ ┣ 📜scyther.png
 ┃ ┃ ┃ ┣ 📜seadra.png
 ┃ ┃ ┃ ┣ 📜seaking.png
 ┃ ┃ ┃ ┣ 📜seel.png
 ┃ ┃ ┃ ┣ 📜shellder.png
 ┃ ┃ ┃ ┣ 📜slowbro.png
 ┃ ┃ ┃ ┣ 📜slowpoke.png
 ┃ ┃ ┃ ┣ 📜snorlax.png
 ┃ ┃ ┃ ┣ 📜spearow.png
 ┃ ┃ ┃ ┣ 📜squirtle.png
 ┃ ┃ ┃ ┣ 📜starmie.png
 ┃ ┃ ┃ ┣ 📜staryu.png
 ┃ ┃ ┃ ┣ 📜tangela.png
 ┃ ┃ ┃ ┣ 📜tauros.png
 ┃ ┃ ┃ ┣ 📜tentacool.png
 ┃ ┃ ┃ ┣ 📜tentacruel.png
 ┃ ┃ ┃ ┣ 📜vaporeon.png
 ┃ ┃ ┃ ┣ 📜venomoth.png
 ┃ ┃ ┃ ┣ 📜venonat.png
 ┃ ┃ ┃ ┣ 📜venusaur.png
 ┃ ┃ ┃ ┣ 📜victreebel.png
 ┃ ┃ ┃ ┣ 📜vileplume.png
 ┃ ┃ ┃ ┣ 📜voltorb.png
 ┃ ┃ ┃ ┣ 📜vulpix.png
 ┃ ┃ ┃ ┣ 📜wartortle.png
 ┃ ┃ ┃ ┣ 📜weedle.png
 ┃ ┃ ┃ ┣ 📜weepinbell.png
 ┃ ┃ ┃ ┣ 📜weezing.png
 ┃ ┃ ┃ ┣ 📜wigglytuff.png
 ┃ ┃ ┃ ┣ 📜zapdos.png
 ┃ ┃ ┃ ┗ 📜zubat.png
 ┃ ┃ ┗ 📜alola.jpg
 ┣ 📜.env.example
 ┣ 📜db.sqlite3
 ┣ 📜download_sprites.py
 ┣ 📜generar_pokedex.py
 ┣ 📜manage.py
 ┣ 📜pokedex.json
 ┗ 📜requirements.txt
