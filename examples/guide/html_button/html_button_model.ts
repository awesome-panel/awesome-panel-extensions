// See https://docs.bokeh.org/en/latest/docs/reference/models/layouts.html
import { HTMLBox, HTMLBoxView } from "models/layouts/html_box"

// See https://docs.bokeh.org/en/latest/docs/reference/core/properties.html
import * as p from "core/properties"

// The view of the Bokeh extension/ HTML element
// Here you can define how to render the model as well as react to model changes or View events.
export class HTMLButtonView extends HTMLBoxView {
    model: HTMLButton
    objectElement: any // Element

    connect_signals(): void {
        super.connect_signals()

        this.connect(this.model.properties.object.change, () => {
            this.render();
        })
    }

    render(): void {
        console.log("render")
        console.log(this.model)
        super.render()
        this.el.innerHTML = this.model.object
        this.objectElement = this.el.firstElementChild

        this.objectElement.addEventListener("click", () => {this.model.clicks+=1;}, false)
    }
}

export namespace HTMLButton {
    export type Attrs = p.AttrsOf<Props>
    export type Props = HTMLBox.Props & {
        object: p.Property<string>,
        clicks: p.Property<number>,
    }
}

export interface HTMLButton extends HTMLButton.Attrs { }

// The Bokeh .ts model corresponding to the Bokeh .py model
export class HTMLButton extends HTMLBox {
    properties: HTMLButton.Props

    constructor(attrs?: Partial<HTMLButton.Attrs>) {
        super(attrs)
    }

    static init_HTMLButton(): void {
        this.prototype.default_view = HTMLButtonView;

        this.define<HTMLButton.Props>({
            object: [p.String, "<button style='width:100%'>Click Me</button>"],
            clicks: [p.Int, 0],
        })
    }
}
