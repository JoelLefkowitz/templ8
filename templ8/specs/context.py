# TODO Redesign context
# @dataclass
# class Context:
#     name: str
#     default: Any = None
#     formatter: Optional[str] = None
#     formatter_kwargs: Optional[Dict[str, Any]] = None

#     def __call__(self, config: Dict) -> str:
#         if self.name in config:
#             lookup = str(config[self.name])
#         elif self.default:
#             lookup = str(self.default)
#         else:
#             raise MissingContext(self.name, config)

#         return (
#             format_str(lookup, self.formatter, **self.formatter_kwargs or {})
#             if self.formatter
#             else lookup
#         )

#     def __repr__(self) -> str:
#         return self.name

#     def encode(self) -> str:
#         kwargs = []
#         if self.default:
#             kwargs.append(f"default={self.default}")

#         if self.formatter:
#             kwargs.append(f"formatter={self.formatter}")

#         if self.formatter_kwargs:
#             kwargs.append(
#                 " ".join([f"{k}={v}" for k, v in self.formatter_kwargs.items()])
#             )

#         return "<" + self.name + " ".join(kwargs) + ">"

#     @classmethod
#     def resolve_in_str(cls: Type[T], string: str, config: Dict) -> str:
#         re_tag = r"<[^<>]*>"
#         return re.sub(re_tag, lambda x: cls.decode(x.group(0))(config), string)

#     @classmethod
#     def decode(cls: Type[T], string: str) -> T:
#         string_parts = string[1:-1].split(" ")
#         name = string_parts.pop(0)
#         kwargs = dict([get_kv(i) for i in string_parts if is_kv(i)])
#         default = kwargs.pop("default", None)
#         formatter = kwargs.pop("formatter", None)
#         formatter_kwargs = kwargs or None
#         return cls(name, default, formatter, formatter_kwargs)

# @dataclass
# class PathReplacement:
#     name: str
#     replacement: str

#     def __call__(self, file_path: str, exclude_head: bool = False) -> str:
#         file_parts = pathlib.Path(file_path).parts
#         replaced_parts = [self.replacement if i == self.name else i for i in file_parts]

#         if exclude_head:
#             replaced_parts[-1] = os.path.split(file_path)[1]
#         return os.path.join(*replaced_parts)

#     def __repr__(self) -> str:
#         return str(self.__dict__)
