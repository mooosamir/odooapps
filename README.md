<?xml version="1.0" encoding="UTF-8"?>
<odoo>
    <data>
        <record id="a_four_report" model="report.paperformat">
            <field name="name">A3 custom</field>
            <field name="default" eval="True"/>
            <field name="format">A4</field>
            <field name="page_height">0</field>
            <field name="page_width">0</field>
            <field name="orientation">Landscape</field>
            <field name="margin_top">25</field>
            <field name="margin_bottom">50</field>
            <field name="margin_left">5</field>
            <field name="margin_right">5</field>
            <field name="header_line" eval="False"/>
            <field name="header_spacing">15</field>
            <field name="dpi">120</field>
        </record>


        <!-- QWeb Reports -->

        <record id="report_custom_cost" model="ir.actions.report">
            <field name="name">Report Custom Cost</field>
            <field name="model">product.template</field>
            <field name="report_type">qweb-pdf</field>
            <field name="report_name">report_cost.template_custom_cost_view</field>
            <field name="report_file">report_cost.template_custom_cost_view</field>
            <field name="binding_model_id" ref="model_product_template"/>
            <field name="paperformat_id" ref="report_cost.a_four_report"/>
            <field name="print_report_name">'Letters Cost'</field>
            <field name="binding_type">report</field>
        </record>

        <template id="template_custom_cost_view">
            <t t-call="web.html_container">
                <t t-if="not o" t-set="o" t-value="doc"/>

                <t t-call="web.basic_layout">
                    <div class="page">
                        <div class="text-center" style="vertical-align : middle;">
                            <h4>Report Letters Cost</h4>
                        </div>
                        <div>
                            <br/>
<!--                            table-condensed-->
                            <table dir="rtl" lang="ar" border="2" cellpadding="0" cellspacing="0" width="100%"
                                   style="min-width: 100%;
                                    font-size: 18px; padding: 0px 8px 0px 8px;"
                                   class="table-bordered" >

                                <thead>
                                    <tr style="">
                                        <th style="text-align:right; vertical-align : middle;">#</th>
                                        <th style="text-align:right; vertical-align : middle;">Product Name</th>
                                        <t t-foreach="docs[0].get_custom_cost_header()" t-as="o">
                                            <th style="text-align:center;">
                                                <div  style="width: 20px%;
                                                padding-top: 50px; -webkit-transform: rotate(90deg);
                                                -moz-transform: rotate(90deg);-o-transform: rotate(90deg);
                                                -ms-transform: rotate(90deg);transform: rotate(90deg);">
                                                    <span t-esc="o" style="display: inline-block;
                                                    word-break: break-word;"/>
                                                </div>
                                            </th>
                                        </t>
                                        <th style="text-align:center; vertical-align : middle;">Total</th>
                                        <th style="text-align:center; vertical-align : middle;">R.Cost</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <t t-set="count" t-value="0"/>
                                    <tr t-foreach="docs" t-as="o"
                                        style="">
                                        <td>
                                            <t t-set="count" t-value="count+1"/>
                                            <t t-esc="count"/>
                                        </td>
                                        <td style="text-align:right;">
                                            <span t-field="o.name"/>
                                        </td>
                                        <t t-foreach="o.get_custom_cost_data()" t-as="p">
                                            <td style="text-align:center;">
                                                <span t-esc="p" t-options='{"widget": "float", "precision": 2}'/>
                                            </td>
                                        </t>
                                        <td style="text-align:center;">
                                                <span t-field="o.standard_price" t-options='{"widget": "float", "precision": 2}'/>
                                            </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </t>
                <div class="article" t-att-data-oe-model="o and o._name" t-att-data-oe-id="o and o.id">
                    <t t-out="0"/>
                </div>
            </t>
        </template>
    </data>
</odoo>
