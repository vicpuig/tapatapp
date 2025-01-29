classDiagram
    class View {
        + requestUsername()
        + showUserData(User)
        + showError(Error)
    }

    class DAOUser {
        + getUserByUsername(username)
    }

    class User {
        +id: int
        +username: String
        +password: String
        +email: String
    }

    class Error {
        +errorCode: int
        +errorJson: JSON
    }
    View --> DAOUser: requests user data
    DAOUser --> View: returns user or error
    DAOUser --> User: retrieves user data
    DAOUser --> Error: retrieves error data if user = None
