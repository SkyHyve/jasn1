class LDAP:

    LDAP_BIND_REQUEST = "LDAP_BIND_REQUEST"
    LDAP_BIND_RESPONSE = "LDAP_BIND_RESPONSE"
    LDAP_UNBIND_REQUEST = "LDAP_UNBIND_REQUEST"
    LDAP_SEARCH_REQUEST = "LDAP_SEARCH_REQUEST"
    LDAP_SEARCH_RESULT_ENTRY = "LDAP_SEARCH_RESULT_ENTRY"
    LDAP_SEARCH_RESULT_DONE = "LDAP_SEARCH_RESULT_DONE"
    LDAP_MODIFY_REQUEST = "LDAP_MODIFY_REQUEST"
    LDAP_MODIFIY_RESPONSE = "LDAP_MODIFIY_RESPONSE"
    LDAP_ADD_REQUEST = "LDAP_ADD_REQUEST"
    LDAP_ADD_RESPONSE = "LDAP_ADD_RESPONSE"
    LDAP_DELETE_REQUEST = "LDAP_DELETE_REQUEST"
    LDAP_DELETE_RESPONSE = "LDAP_DELETE_RESPONSE"
    LDAP_MODIFY_DN_REQUEST = "LDAP_MODIFY_DN_REQUEST"
    LDAP_MODIFY_DN_RESPONSE = "LDAP_MODIFY_DN_RESPONSE"
    LDAP_COMPARE_REQUEST = "LDAP_COMPARE_REQUEST"
    LDAP_COMPARE_RESPONSE = "LDAP_COMPARE_RESPONSE"

    TYPE_MAP = {
        0: LDAP_BIND_REQUEST,
        1: LDAP_BIND_RESPONSE,
        2: LDAP_UNBIND_REQUEST,
        3: LDAP_SEARCH_REQUEST,
        4: LDAP_SEARCH_RESULT_ENTRY,
        5: LDAP_SEARCH_RESULT_DONE,
        6: LDAP_MODIFY_REQUEST,
        7: LDAP_MODIFIY_RESPONSE,
        8: LDAP_ADD_REQUEST,
        9: LDAP_ADD_RESPONSE,
        10: LDAP_DELETE_REQUEST,
        11: LDAP_DELETE_RESPONSE,
        12: LDAP_MODIFY_DN_REQUEST,
        13: LDAP_MODIFY_DN_RESPONSE,
        14: LDAP_COMPARE_REQUEST,
        15: LDAP_COMPARE_RESPONSE,
    }

    LDAP_SUCCESS = "LDAP_SUCCESS"
    LDAP_OPERATIONS_ERROR = "LDAP_OPERATIONS_ERROR"

    def parse_tag_type(node: tuple, tag: int):
        if node == (1,):
            if TYPE_MAP.get(tag) is None:
                raise NotImplementedError("LDAP tag type {tag} has no mapping".format(tag=tag))
            return TYPE_MAP[tag]
        else:
            return None

    def parse_value(node: tuple, tag_type: str, value: int):
        if node == (1, 0) and tag_type == "ENUMERATED":
            if value == 0:
                value = LDAP_SUCCESS
            elif value == 1:
                value = LDAP_OPERATIONS_ERROR

        return value
LDAP.INVERSE_TYPE_MAP = {LDAP.TYPE_MAP[x]: x for x in LDAP.TYPE_MAP}
