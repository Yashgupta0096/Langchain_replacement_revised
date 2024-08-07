import AvatarGenerator from 'components/AvatarGenerator/AvatarGenerator'
import MemberText from 'modals/AIChatModal/components/ChatMembers/components/MemberText'

import IconButton from '@l3-lib/ui-core/dist/IconButton'
import Edit from '@l3-lib/ui-core/dist/icons/Edit'
import EyeOpen from '@l3-lib/ui-core/dist/icons/EyeOpen'
import styled, { css } from 'styled-components'
import {
  StyledDeleteIcon,
  StyledEditIcon,
  StyledEyeOpenIcon,
} from 'pages/TeamOfAgents/TeamOfAgentsCard/TeamOfAgentsCard'

type TeamChatCardProps = {
  onClick: () => void
  onViewClick: () => void
  onEditClick?: () => void
  onDeleteClick?: () => void
  picked: boolean
  team: any
  agents: any
}

const TeamChatCard = ({
  onClick,
  picked,
  onViewClick,
  onEditClick,
  onDeleteClick,
  team,
  agents,
}: TeamChatCardProps) => {
  const handleEdit = (event: any) => {
    event.stopPropagation()
    if (onEditClick) {
      onEditClick()
    }
  }

  const handleView = (event: any) => {
    event.stopPropagation()
    onViewClick()
  }

  const handleDelete = (event: any) => {
    event.stopPropagation()
    if (onDeleteClick) {
      onDeleteClick()
    }
  }

  return (
    <StyledAgentWrapper onClick={onClick} picked={picked}>
      <AvatarGenerator name={team?.name} size={30} avatar={team.avatar} />
      <MemberText name={team?.name} role={team.team_type} />

      {/* <StyledTeamAgents>
        {agents?.map((agent: any, index: number) => {
          return (
            <StyledAgent key={index}>
              <AvatarGenerator name={agent?.agent?.name} avatar={agent?.agent?.avatar} size={20} />
            </StyledAgent>
          )
        })}
      </StyledTeamAgents> */}

      <StyledIconButtonWrapper className='hiddenButton'>
        {onDeleteClick && (
          <IconButton
            onClick={handleDelete}
            icon={() => <StyledDeleteIcon />}
            size={IconButton.sizes.SMALL}
            kind={IconButton.kinds.TERTIARY}
            // ariaLabel='Delete'
          />
        )}

        <IconButton
          onClick={handleView}
          icon={() => (
            <StyledIconWrapper>
              <StyledEyeOpenIcon size={50} />
            </StyledIconWrapper>
          )}
          size={IconButton.sizes.SMALL}
          kind={IconButton.kinds.TERTIARY}
          // ariaLabel='View'
        />

        {onEditClick && (
          <IconButton
            onClick={handleEdit}
            icon={() => <StyledEditIcon />}
            size={IconButton.sizes.SMALL}
            kind={IconButton.kinds.TERTIARY}
            // ariaLabel='Edit'
          />
        )}
      </StyledIconButtonWrapper>
    </StyledAgentWrapper>
  )
}

export default TeamChatCard

export const StyledAgentWrapper = styled.div<{ picked: boolean }>`
  cursor: pointer;

  display: flex;
  align-items: center;
  gap: 5px;

  padding: 10px;
  width: 100%;
  max-width: 350px;

  /* background: rgba(255, 255, 255, 0.1); */

  padding-left: 15px;
  border-radius: 10px;

  :hover {
    background: rgba(0, 0, 0, 0.1);
    .hiddenButton {
      opacity: 1;
    }
  }

  ${props =>
    props.picked &&
    css`
      background: ${({ theme }) => theme.body.teamChatCardSelectedColor};
      :hover {
        background: ${({ theme }) => theme.body.teamChatCardSelectedColor};
      }
    `}
`

export const StyledIconWrapper = styled.div`
  color: transparent;
`

export const StyledIconButtonWrapper = styled.div`
  margin-left: auto;

  opacity: 0;
  /* transition: opacity 300ms; */

  display: flex;
  align-items: center;
`

export const StyledTeamAgents = styled.div`
  /* height: 100%; */
  display: flex;
`
const StyledAgent = styled.div`
  margin-right: -8px;
`
