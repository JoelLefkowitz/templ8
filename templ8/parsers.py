from yummy_cereal import AnotatedFieldsParser

from pyimport import path_guard

path_guard("..")
from models import Spec, Context, PathReplacement, Callback


required_context_parser = AnotatedFieldsParser(
    cls=Context, collector_field="default", collect_with_names=True
)

path_replacements_parser = AnotatedFieldsParser(
    cls=PathReplacement, parse_as_named=True, inner_named_field="replacement"
)

callbacks_parser = AnotatedFieldsParser(
    cls=Callback, parse_as_named=True, inner_named_field="call"
)

spec_parser = AnotatedFieldsParser(
    cls=Spec,
    typed_parsers={
        Context: required_context_parser,
        PathReplacement: path_replacements_parser,
        Callback: callbacks_parser,
    },
)
