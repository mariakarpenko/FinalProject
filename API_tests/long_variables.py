# Длинные переменные

string_501_symbols = "ппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппп"

query_string = """query search($search: String!, $cursor: String!, $type: Type, $noMisspell: Boolean) {
  search(
    query: {cursor: $cursor, query: $search, type: $type, noMisspell: $noMisspell}
  ) {
    cursor
    misspell {
      correctedText
      correctionType
      __typename
    }
    page {
      ... on AudioBook {
        listenersCount
        book {
          ...SearchBook
          __typename
        }
        narrators {
          ...SearchAuthor
          __typename
        }
        progress {
          ...BookProgress
          __typename
        }
        __typename
      }
      ... on ComicBook {
        readersCount
        book {
          ...SearchBook
          __typename
        }
        progress {
          ...BookProgress
          __typename
        }
        __typename
      }
      ... on TextBook {
        readersCount
        book {
          ...SearchBook
          __typename
        }
        progress {
          ...BookProgress
          __typename
        }
        __typename
      }
      ... on Bookshelf {
        uuid
        name
        followersCount
        cover {
          ...SearchAvatar
          __typename
        }
        description
        posts {
          total
          __typename
        }
        user {
          uuid
          avatar {
            ...SearchAvatar
            __typename
          }
          name
          __typename
        }
        __typename
      }
      ... on Series {
        uuid
        name
        cover {
          ...SearchAvatar
          __typename
        }
        items {
          total
          __typename
        }
        authors {
          ...SearchAuthor
          __typename
        }
        __typename
      }
      ... on TextSerial {
        readersCount
        book {
          ...SearchBook
          __typename
        }
        episodes {
          total
          __typename
        }
        progress {
          ...BookProgress
          __typename
        }
        __typename
      }
      ... on Person {
        name
        uuid
        roles
        worksCount
        author {
          totalBook
          __typename
        }
        narrator {
          totalBook
          __typename
        }
        translator {
          totalBook
          __typename
        }
        avatar {
          ...SearchAvatar
          __typename
        }
        __typename
      }
      ... on Topic {
        name
        uuid
        totalBook
        slug
        parent {
          slug
          name
          __typename
        }
        __typename
      }
      ... on User {
        name
        uuid
        login
        followersCount
        avatar {
          ...SearchAvatar
          __typename
        }
        __typename
      }
      ... on Publisher {
        name
        uuid
        worksCount
        avatar {
          ...SearchAvatar
          __typename
        }
        __typename
      }
      __typename
    }
    __typename
  }
}

fragment SearchBook on Book {
  uuid
  name
  annotation
  ageRestriction
  cover {
    ...SearchAvatar
    __typename
  }
  topics {
    name
    totalBook
    uuid
    __typename
  }
  publisher {
    uuid
    name
    avatar {
      ...SearchAvatar
      __typename
    }
    __typename
  }
  translators {
    uuid
    name
    narrator {
      totalBook
      __typename
    }
    author {
      totalBook
      __typename
    }
    author {
      totalBook
      __typename
    }
    translator {
      totalBook
      __typename
    }
    avatar {
      ...SearchAvatar
      __typename
    }
    __typename
  }
  authors {
    ...SearchAuthor
    __typename
  }
  __typename
}

fragment SearchAvatar on Cover {
  url
  ratio
  backgroundColorHex
  __typename
}

fragment SearchAuthor on Person {
  uuid
  avatar {
    ...SearchAvatar
    __typename
  }
  author {
    totalBook
    __typename
  }
  name
  roles
  narrator {
    totalBook
    __typename
  }
  translator {
    totalBook
    __typename
  }
  __typename
}

fragment BookProgress on Progress {
  inLibrary
  finished
  progress
  __typename
}"""