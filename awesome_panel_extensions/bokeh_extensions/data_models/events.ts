import { HTMLBox, HTMLBoxView } from "@bokehjs/models/layouts/html_box"

import * as p from "@bokehjs/core/properties"

export class IntegerEventView extends HTMLBoxView {
    model: any;
    element: any;

    render(): void {
        super.render()

        this.element = <any>document.getElementById(this.model.element);
        if (this.element===null){
            this.element = <any>document.querySelector(this.model.element);
        }
        if (this.element===null){return}

        if (this.model.event!=null && this.model.event!==""){
            const view=this;
            this.element.addEventListener(this.model.event, function() {
                view.model.value+=1;
            });
        }
    }
}

export namespace IntegerEvent {
    export type Attrs = p.AttrsOf<Props>
    export type Props = HTMLBox.Props & {
        element: p.Property<string>;
        event: p.Property<string>;
        value: p.Property<number>;
    }
}

export interface IntegerEvent extends IntegerEvent.Attrs { }

export class IntegerEvent extends HTMLBox {
    properties: IntegerEvent.Props

    constructor(attrs?: Partial<IntegerEvent.Attrs>) {
        super(attrs)
    }

    static __module__ = "awesome_panel_extensions.bokeh_extensions.data_models.events"

    static init_IntegerEvent(): void {
        this.prototype.default_view = IntegerEventView;

        this.define<IntegerEvent.Props>({
            element: [p.String, ],
            event: [p.String, ],
            value: [p.Int, ],
        })
    }
}

