# Package design

This file introduces a structure definition for the packages forming the backbone of the client-server communication.
Example JSONs that are provided are meant as a reference, not test JSONs as they contain invalid elements such as comments.


### general package structure


A package is defined as a valid JSON string containing a package `type` as well as a `body` which holds the package specific information.

The ASCII record seperator (`\x1e`, ASCII 30) is used to seperate individual JSON objects.

example JSON:
```json
{
	"type":		"name",
	"body":
	{
        // package specific information
	}
}
```


# Client -> Server

packages sent from client to server

<details>
<summary>overview</summary>

| Package Type                                        | Game Stage  | Sent On    | Max Times Sent |
|-----------------------------------------------------|-------------|------------|----------------|
| [start-game-session](#start-game-session)           | before game | event      | 1              |
| [connect-to-game-session](#connect-to-game-session) | before game | event      | 1[^1]          |
| [status-update](#status-update)                     | lobby       | event      | N              |
| [player-clicks](#player-clicks)                     | game        | periodical | N              |

[^1]: package can be sent N times but only once succefully.

</details>



### pre-game start

packages sent pre-game and pre-lobby

<div id="start-game-session">
<details>
<summary>start game session</summary>

This package is sent when a <ins>new</ins> game session is initiated.
The package initiates AND joins the player in the session.
`playername` can be any string. Any validation is to be performed server-side but is not currently planned.
This package is sent only once and is event-driven.

Example JSON:
```json
{
	"type":		"start-game-session",
	"body":
	{
		"playername":	"passcht_03"
	}
}
```
</details>
</div>

<div id="connect-to-game-session">
<details>
<summary>connect to game session</summary>

This package is sent when a player wants to connect to an <ins>existing</ins> game session.
The `gamecode` is a string validated on the server side.
`playername` can be any string. Any validation is to be performed server-side but is not currently planned.
This package is sent only once and is event-driven.

```json
{
    "type":		"connect-to-game-session",
	"body":
	{
		"gamecode":	"A0313",
		"playername":	"passcht_03"
	}
}
```
</details>
</div>


### lobby loop
packages sent in the lobby.

<div id="status-update">
<details>
<summary>status update</summary>

This package is sent when a individual player changes their 'readiness' status.
It can be sent N times per player and is event-driven.

```json
{
	"type":		"status-update",
	"body":
	{
		"is-ready": true
	}
}
```
</details>
</div>


### game loop

<div id="player-clicks">
<details>
<summary>player clicks</summary>

This package is sent perdiodically and contains the <ins>raw clicks since last package</ins>.

```json
{
	"type":		"player-clicks",
	"body":
	{
		"count": 5
	}
}
```
</details>
</div>


# Server -> Client

<details>
<summary>overview</summary>

| Package Type                      | Game Stage | Sent On    | Max Times Sent |
|-----------------------------------|------------|------------|----------------|
| [exception](#exception)           | global     | event      | N              |
| [lobby-status](#lobby-status)     | lobby      | periodical | N              |
| [game-start](#game-start)         | lobby      | event      | 1              |
| [game-update](#game-update)       | game       | periodical | N              |
| [end-routine](#end-routine)       | postgame   | event      | 1              |

</details>


### general

<div id="exception">
<details>
<summary>Exception</summary>

This package is sent to the client when an exception occurs.
`details` is an object with an undertermined structure and provides additional information depending on the specific exception that occured. 

```json
{
    "type": "exception",
    "body": {
        "name": "gamecode-not-found",
        "details": {}  //additional exception details
    }
}
```

</details>
</div>




### lobby loop

<div id="lobby-status">
<details>
<summary>lobby-status</summary>

This package is sent periodically to indicate the current status of the lobby.

```json
{
    "type": "lobby-status",
    "body": {
        "gamecode": "A0313",
        "players": [
            {
                "playername": "player1",
                "is-ready": true
            },
            {
                "playername": "player2",
                "is-ready": false
            }
        ]
    }
}
```
</details>
</div>


<details>
<summary>game-start</summary>

This package is sent to indicate a game start.

```json
{
    "type": "game-start",
    "body": {
    }
}
```
</details>
</div>



### game loop

<div id="game-update">
<details>
<summary>game-update</summary>

This package is sent on a schedule and is customized per player.  
`top-players` is an array ordered by score descending.

```json
{
    "type": "game-update",
    "body": {
        "currency": 4738.43,
        "score": 709.2,
        "top-players": [
            {
                "playername": "p5",
                "score": 7979.6
            },
            {
                "playername": "p1",
                "score": 6000.6
            },
            {
                "playername": "p2",
                "score": 5037
            }
        ]
    }
}
```
</details>
</div>

### end routine

<div id="end-routine">
<details>
<summary>end-routine</summary>

This package is sent once after the game ends, customized per player.  
`scoreboard` is an array ordered by score descending.

```json
{
    "type": "end-routine",
    "body": {
        "score": 709.2,
        "is-winner": false,
        "scoreboard": [
            {
                "playername": "p5",
                "score": 7979.6
            },
            {
                "playername": "p1",
                "score": 6000.6
            },
            {
                "playername": "p2",
                "score": 5037
            },
            {
                "playername": "player N",
                "score": 1000
            }
        ]
    }
}
```
</details>
</div>

