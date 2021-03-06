# vim:fileencoding=utf-8

from django.conf.urls import patterns, url

urlpatterns = patterns('iprestrict.views',
    url(r'^$', 'test_rules_page'),
    url(r'^move_rule_up/(?P<rule_id>\d+)[/]?$', 'move_rule_up'),
    url(r'^move_rule_down/(?P<rule_id>\d+)[/]?$', 'move_rule_down'),
    url(r'^reload_rules[/]?$', 'reload_rules'),
    url(r'^test_match[/]?$', 'test_match'),
)

