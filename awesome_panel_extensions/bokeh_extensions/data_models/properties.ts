import { HTMLBox, HTMLBoxView } from "@bokehjs/models/layouts/html_box"

import * as p from "@bokehjs/core/properties"

export class PropertyModelView extends HTMLBoxView {
    model: any;
    element: any;

    connect_signals(): void {
        super.connect_signals()

        this.connect(this.model.properties.value.change, this.updateElement)
    }

    private updateElement() {
        if (this.element){
            const newValue = this.model.value;
            const oldValue = this.element[this.model.property_]
            if (newValue!==oldValue){
                this.element[this.model.property_]=newValue;
            }
        }
      }

    render(): void {
        super.render()

        this.element = <any>document.getElementById(this.model.element);
        if (this.element===null){
            this.element = <any>document.querySelector(this.model.element);
        }
        if (this.element===null){return}

        this.updateElement();

        if (this.model.event!=null && this.model.event!==""){
            const view=this;
            this.element.addEventListener(this.model.event, function() {
                const newValue = view.element[view.model.property_]
                const oldValue = view.model.value;
                if (newValue!==oldValue){
                    view.model.value=newValue;
                }
            });
        }
    }
}

export namespace PropertyModel {
    export type Attrs = p.AttrsOf<Props>
    export type Props = HTMLBox.Props & {
        element: p.Property<string>;
        event: p.Property<string>;
        property_: p.Property<string>;
        // value: p.Property<string>;
    }
}

export interface PropertyModel extends PropertyModel.Attrs { }

export class PropertyModel extends HTMLBox {
    properties: PropertyModel.Props

    constructor(attrs?: Partial<PropertyModel.Attrs>) {
        super(attrs)
    }

    static __module__ = "awesome_panel_extensions.bokeh_extensions.data_models.properties"

    static init_PropertyModel(): void {
        this.prototype.default_view = PropertyModelView;

        this.define<PropertyModel.Props>({
            element: [p.String, ],
            event: [p.String, ],
            property_: [p.String, ],
            // value: [p.String, ],
        })
    }
}

export class StringPropertyView extends PropertyModelView {
    model: StringProperty
}

export namespace StringProperty {
    export type Attrs = p.AttrsOf<Props>
    export type Props = PropertyModel.Props & {
        value: p.Property<string>;
    }
}

export interface StringProperty extends StringProperty.Attrs { }

export class StringProperty extends PropertyModel {
    properties: StringProperty.Props

    constructor(attrs?: Partial<StringProperty.Attrs>) {
        super(attrs)
    }

    static init_StringProperty(): void {
        this.prototype.default_view = StringPropertyView;

        this.define<StringProperty.Props>({
            value: [p.String, ],
        })
    }
}

export class BooleanPropertyView extends PropertyModelView {
    model: BooleanProperty
}

export namespace BooleanProperty {
    export type Attrs = p.AttrsOf<Props>
    export type Props = PropertyModel.Props & {
        value: p.Property<boolean>;
    }
}

export interface BooleanProperty extends BooleanProperty.Attrs { }

export class BooleanProperty extends PropertyModel {
    properties: BooleanProperty.Props

    constructor(attrs?: Partial<BooleanProperty.Attrs>) {
        super(attrs)
    }

    static init_BooleanProperty(): void {
        this.prototype.default_view = BooleanPropertyView;

        this.define<BooleanProperty.Props>({
            value: [p.Boolean, ],
        })
    }
}

export class IntegerPropertyView extends PropertyModelView {
    model: IntegerProperty
}

export namespace IntegerProperty {
    export type Attrs = p.AttrsOf<Props>
    export type Props = PropertyModel.Props & {
        value: p.Property<number>;
    }
}

export interface IntegerProperty extends IntegerProperty.Attrs { }

export class IntegerProperty extends PropertyModel {
    properties: IntegerProperty.Props

    constructor(attrs?: Partial<IntegerProperty.Attrs>) {
        super(attrs)
    }

    static init_IntegerProperty(): void {
        this.prototype.default_view = IntegerPropertyView;

        this.define<IntegerProperty.Props>({
            value: [p.Int, ],
        })
    }
}

export class FloatPropertyView extends PropertyModelView {
    model: FloatProperty
}

export namespace FloatProperty {
    export type Attrs = p.AttrsOf<Props>
    export type Props = PropertyModel.Props & {
        value: p.Property<number>;
    }
}

export interface FloatProperty extends FloatProperty.Attrs { }

export class FloatProperty extends PropertyModel {
    properties: FloatProperty.Props

    constructor(attrs?: Partial<FloatProperty.Attrs>) {
        super(attrs)
    }

    static init_FloatProperty(): void {
        this.prototype.default_view = FloatPropertyView;

        this.define<FloatProperty.Props>({
            value: [p.Number, ],
        })
    }
}

export class ListPropertyView extends PropertyModelView {
    model: ListProperty
}

export namespace ListProperty {
    export type Attrs = p.AttrsOf<Props>
    export type Props = PropertyModel.Props & {
        value: p.Property<any>;
    }
}

export interface ListProperty extends ListProperty.Attrs { }

export class ListProperty extends PropertyModel {
    properties: ListProperty.Props

    constructor(attrs?: Partial<ListProperty.Attrs>) {
        super(attrs)
    }

    static init_ListProperty(): void {
        this.prototype.default_view = ListPropertyView;

        this.define<ListProperty.Props>({
            value: [p.Array, ],
        })
    }
}

export class DictPropertyView extends PropertyModelView {
    model: DictProperty
}

export namespace DictProperty {
    export type Attrs = p.AttrsOf<Props>
    export type Props = PropertyModel.Props & {
        value: p.Property<any>;
    }
}

export interface DictProperty extends DictProperty.Attrs { }

export class DictProperty extends PropertyModel {
    properties: DictProperty.Props

    constructor(attrs?: Partial<DictProperty.Attrs>) {
        super(attrs)
    }

    static init_DictProperty(): void {
        this.prototype.default_view = DictPropertyView;

        this.define<DictProperty.Props>({
            value: [p.Any, ],
        })
    }
}

