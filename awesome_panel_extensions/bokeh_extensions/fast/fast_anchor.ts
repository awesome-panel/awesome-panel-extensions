import { HTMLBox, HTMLBoxView } from "@bokehjs/models/layouts/html_box"

import * as p from "@bokehjs/core/properties"

export class FastAnchorView extends HTMLBoxView {
    model: FastAnchor
    anchor_el: HTMLElement // Element

    setAttr(attribute: string, value: string|null): void {
        const anchor_el = <any>this.anchor_el;
        if (value===null){
            anchor_el.setAttribute(attribute, false)
        } else {
            anchor_el.setAttribute(attribute, value)
        }
    }

    connect_signals(): void {
        super.connect_signals()

        this.connect(this.model.properties.name.change, () => {
            if (this.model.name===null){
                this.anchor_el.innerHTML="";
            } else {
                this.anchor_el.innerHTML=this.model.name
            }
        })
        this.connect(this.model.properties.appearance.change, () => {
            this.setAttr("appearance", this.model.appearance)
        })
        this.connect(this.model.properties.href.change, () => {
            this.setAttr("href", this.model.href)
        })

        this.connect(this.model.properties.hreflang.change, () => {
            this.setAttr("hreflang", this.model.hreflang)
        })
        this.connect(this.model.properties.ping.change, () => {
            this.setAttr("ping", this.model.ping)
        })
        this.connect(this.model.properties.href.change, () => {
            this.setAttr("referrerpolicy", this.model.referrerpolicy)
        })

        this.connect(this.model.properties.download.change, () => {
            this.setAttr("download", this.model.download)
        })
        this.connect(this.model.properties.referrer.change, () => {
            this.setAttr("referrer", this.model.referrer)
        })
        this.connect(this.model.properties.rel.change, () => {
            this.setAttr("rel", this.model.rel)
        })
        this.connect(this.model.properties.target.change, () => {
            this.setAttr("mimetype", this.model.mimetype)
        })
    }

    render(): void {
        super.render()
        const anchor_el = <any>document.createElement("fast-anchor")
        this.anchor_el = <HTMLElement>anchor_el
        this.anchor_el.style.width="100%"
        this.el.appendChild(this.anchor_el)

        if (this.model.name!==null){this.anchor_el.innerHTML=this.model.name}
        if (this.model.appearance!==null){anchor_el.appearance=this.model.appearance}
        if (this.model.href!==null){anchor_el.href=this.model.href}
        if (this.model.hreflang!==null){anchor_el.hreflang=this.model.hreflang}
        if (this.model.ping!==null){anchor_el.ping=this.model.ping}
        if (this.model.referrerpolicy!==null){anchor_el.referrerpolicy=this.model.referrerpolicy}
        if (this.model.download!==null){anchor_el.download=this.model.download}
        if (this.model.referrer!==null){anchor_el.ref=this.model.referrer}
        if (this.model.rel!==null){anchor_el.rel=this.model.rel}
        if (this.model.target!==null){anchor_el.target=this.model.target}
        if (this.model.mimetype!==null){anchor_el.mimetype=this.model.mimetype}




    }
}

export namespace FastAnchor {
    export type Attrs = p.AttrsOf<Props>
    export type Props = HTMLBox.Props & {
        appearance: p.Property<string>;
        download: p.Property<string>;
        href: p.Property<string>;
        hreflang: p.Property<string>;
        ping: p.Property<string>;
        referrerpolicy: p.Property<string>;
        referrer: p.Property<string>;
        rel: p.Property<string>;
        target: p.Property<string>;
        mimetype: p.Property<string>;
    }
}

export interface FastAnchor extends FastAnchor.Attrs { }

export class FastAnchor extends HTMLBox {
    properties: FastAnchor.Props

    constructor(attrs?: Partial<FastAnchor.Attrs>) {
        super(attrs)
    }

    static __module__ = "awesome_panel_extensions.bokeh_extensions.fast.fast_anchor"

    static init_FastAnchor(): void {
        this.prototype.default_view = FastAnchorView;

        this.define<FastAnchor.Props>({
            appearance: [p.String, ],
            download: [p.String, ],
            href: [p.String, ],
            hreflang: [p.String, ],
            ping: [p.String, ],
            referrerpolicy: [p.String, ],
            referrer: [p.String, ], // cannot call this ref
            rel: [p.String, ],
            target: [p.String, ],
            mimetype: [p.String, ],
        })
    }
}