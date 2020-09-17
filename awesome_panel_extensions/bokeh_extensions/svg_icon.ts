import {AbstractIcon, AbstractIconView} from "@bokehjs/models/widgets/abstract_icon"
import * as p from "@bokehjs/core/properties"

// See https://stackoverflow.com/questions/494143/creating-a-new-dom-element-from-an-html-string-using-built-in-dom-methods-or-pro
/**
 * @param {String} HTML representing a single element
 * @return {Element}
 */
function htmlToElement(html: string) {
  var template = document.createElement('template');
  html = html.trim(); // Never return a text node of whitespace as the result
  template.innerHTML = html;
  return <HTMLElement>template.content.firstChild;
}

export class SVGIconView extends AbstractIconView {
  model: SVGIcon

  connect_signals(): void {
    super.connect_signals()
    this.connect(this.model.change, () => this.render())
  }

  render(): void {
    super.render()

    if (this.model.svg===null && this.model.svg===""){return}
    const el = htmlToElement(this.model.svg)
    this.el.innerHTML=""
    this.el.appendChild(el)
    this.el.style.display = "inline"
    this.el.style.verticalAlign = "middle"
    el.style.height = `${this.model.size}em`
    el.style.width = `${this.model.size}em`
    el.style.fill = this.model.fill_color
    if (this.model.spin_duration>0){
      // See https://codepen.io/eveness/pen/BjLaoa
      const animationDuration = `${this.model.spin_duration}ms`

      el.style.setProperty("-webkit-animation-name", "spin")
      el.style.setProperty("-webkit-animation-duration", animationDuration)
      el.style.setProperty("-webkit-animation-iteration-count", "infinite")
      el.style.setProperty("-webkit-animation-timing-function", "linear")
      el.style.setProperty("-moz-animation-name", "spin")
      el.style.setProperty("-moz-animation-duration", animationDuration)
      el.style.setProperty("-moz-animation-iteration-count", "infinite")
      el.style.setProperty("-moz-animation-timing-function", "linear")
      el.style.setProperty("-ms-animation-name", "spin")
      el.style.setProperty("-ms-animation-duration", animationDuration)
      el.style.setProperty("-ms-animation-iteration-count", "infinite")
      el.style.setProperty("-ms-animation-timing-function", "linear")
      el.style.setProperty("animation-name", "spin")
      el.style.setProperty("animation-duration", animationDuration)
      el.style.setProperty("animation-iteration-count", "infinite")
      el.style.setProperty("animation-timing-function", "linear")

    }
    el.classList.add("icon")
    if (this.model.icon_name!=null && this.model.icon_name!==""){
      el.classList.add(`icon-${this.model.icon_name}`)
    }
  }
}

export namespace SVGIcon {
  export type Attrs = p.AttrsOf<Props>

  export type Props = AbstractIcon.Props & {
    icon_name: p.Property<string>;
    svg: p.Property<string>;
    size: p.Property<number>;
    fill_color: p.Property<string>;
    spin_duration: p.Property<number>;
  }
}

export interface SVGIcon extends SVGIcon.Attrs {}

export class SVGIcon extends AbstractIcon {
  properties: SVGIcon.Props

  constructor(attrs?: Partial<SVGIcon.Attrs>) {
    super(attrs)
  }

  static __module__ = "awesome_panel_extensions.bokeh_extensions.svg_icon"

  static init_SVGIcon(): void {
    this.prototype.default_view = SVGIconView

    this.define<SVGIcon.Props>({
        icon_name: [p.String, ],
        svg: [p.String, ],
        size:      [ p.Number, 1.0 ],
        fill_color: [ p.String, "currentColor"],
        spin_duration: [ p.Number, 0.0 ],
    })
  }
}