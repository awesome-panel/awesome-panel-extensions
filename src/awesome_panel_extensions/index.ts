import * as AwesomePanelExtensions from "./bokeh_extensions"
export {AwesomePanelExtensions}

import {register_models} from "@bokehjs/base"
register_models(AwesomePanelExtensions as any)