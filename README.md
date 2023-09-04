# Sphinx – heading with `:manpage:` bug

This repository contains the minimal example to demonstrate a sphinx bug
when using `:manpage:` in a heading.

When using `:manpage:` in a heading in `reStructuredText`, the manpage properties for the node does not get parsed.

For example:

```reStructuredText
:manpage:`ls(1)`
----------------
```

results in an error like:

```
Exception occurred:
  File "/path/to/project/.sphinx/venv/lib/python3.10/site-packages/sphinx/writers/html5.py", line 749, in visit_manpage
    node['refuri'] = self.manpages_url.format(**node.attributes)
KeyError: 'section'
```

## Debugging

Attaching a debugger showed that the manpage node attributes were not parsed:

```
> /path/to/project/docs/.sphinx/venv/lib/python3.10/site-packages/sphinx/writers/html5.py(751)visit_manpage()
-> node['refuri'] = self.manpages_url.format(**node.attributes)
(Pdb) node
<manpage: <#text: 'ls(1)'>>
(Pdb) node.attributes
{'ids': [], 'classes': ['manpage'], 'names': [], 'dupnames': [], 'backrefs': [], 'xml:space': 'preserve'}
```