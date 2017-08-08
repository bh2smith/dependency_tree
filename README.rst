Description:
============

Dependency trees are a great way to visualize all the odoo-modules required
for yours to survive in the wild. In some cases, you may find that there are
redundancies and help trim the fat.

In fact, this module already demonstrates that there are several redundant
dependencies to 'base'. Observe the visualization of the dependency tree for
the core odoo module *Discuss* appears as follows

.. code-block::
    |base
    |base_setup
    |----base
    |----web_kanban
    |--------web
    |------------base
    |bus
    |----base
    |----web
    |--------base
    |web_tour
    |----web
    |--------base


Notice, it depends on base along with each of the other first level dependencies?

Same applies for 'bus' and 'base_setup' as depicted in the visualization.

Now go and try removing the 'base' dependency from each of

- /odoo/addons/mail/__manifest__.py
- /odoo/addons/base_setup/__manifest__.py
- /odoo/addons/bus/__manifest__.py

and find that the entire mail / "Discuss" Module remains totally stable!

This applies to several core odoo modules,

- base_action_rule
- calendar
- sales team

and those are just a few I was able to dig up with this module in 5 minutes.

It appears also that CRM has some other redundant dependencies such as

- base_action_rule
- base_setup
- web_tour

In Calendar we can remove

- base
- mail

Known Issues
============

As a majority of fields are uniquely determined by the choice of source/root
module, they are unfortunately computed and stored. This implies that we can
not gain any further visualization through a graph view.

This could be avoided, by first selecting a module through a wizard, processing
calculations and then creating the objects as read-only.
