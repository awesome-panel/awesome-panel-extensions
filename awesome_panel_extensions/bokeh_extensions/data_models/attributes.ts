import { HTMLBox, HTMLBoxView } from "@bokehjs/models/layouts/html_box"

import * as p from "@bokehjs/core/properties"

export class StringAttributeView extends HTMLBoxView {
    model: StringAttribute;
    element: any;

    connect_signals(): void {
        super.connect_signals()

        this.connect(this.model.properties.value.change, this.updateElement)
    }

    private updateElement() {
        if (this.element){
            const newValue = this.model.value;
            const oldValue = this.element.getAttribute(this.model.attribute);
            console.log(["updateElement", oldValue, newValue]);
            if (newValue!==oldValue){
                this.element.setAttribute(this.model.attribute, newValue);
            }
        }
      }

    render(): void {
        console.log("render");
        super.render()

        this.element = <any>document.getElementById(this.model.element);
        if (this.element===null){
            this.element = <any>document.querySelector(this.model.element);
        }
        if (this.element===null){return}

        this.updateElement();

        this.addAttributesMutationObserver();
    }

    addAttributesMutationObserver(): void {
        let options = {
          childList: false,
          attributes: true,
          characterData: false,
          subtree: false,
          attributeFilter: [this.model.attribute],
          attributeOldValue: false,
          characterDataOldValue: false
        };

        const handleAttributeChange = (_: Array<MutationRecord>): void => {
            var newValue = this.element.getAttribute(this.model.attribute);
            if (newValue===true || newValue===false){
                newValue="";
            }
            const oldValue = this.model.value;
            console.log(["handleAttributeChange", oldValue, newValue]);
            if (newValue!==oldValue){
                this.model.value=newValue;
            }
        }

        let observer = new MutationObserver(handleAttributeChange)
        observer.observe(this.element, options)
      }
}

export namespace StringAttribute {
    export type Attrs = p.AttrsOf<Props>
    export type Props = HTMLBox.Props & {
        element: p.Property<string>;
        event: p.Property<string>;
        attribute: p.Property<string>;
        value: p.Property<string>;
    }
}

export interface StringAttribute extends StringAttribute.Attrs { }

export class StringAttribute extends HTMLBox {
    properties: StringAttribute.Props

    constructor(attrs?: Partial<StringAttribute.Attrs>) {
        super(attrs)
    }

    static __module__ = "awesome_panel_extensions.bokeh_extensions.data_models.attributes"

    static init_StringAttribute(): void {
        this.prototype.default_view = StringAttributeView;

        this.define<StringAttribute.Props>({
            element: [p.String, ],
            event: [p.String, ],
            attribute: [p.String, ],
            value: [p.String, ],
        })
    }
}
